from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    publication_date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name='Категория')
    tags = models.ManyToManyField("Tag", related_name='article',  verbose_name='Теги')
    likes_count = models.IntegerField(default=0)
    favourites_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True,  verbose_name='Теги')
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='articles/%Y/%m/%d/',
                              validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'jpeg'])],
                              blank=True,
                              null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while Article.objects.exclude(id=self.id).filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'  # единственное число для отображения в админке
        verbose_name_plural = 'Статьи'  # мн. число для отображения в админке

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'  # единственное число для отображения в админке
        verbose_name_plural = 'Категории'  # мн. число для отображения в админке

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'  # единственное число для отображения в админке
        verbose_name_plural = 'Теги'  # мн. число для отображения в админке

class ArticleUserMananger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def sorted_by_abc(self):
        return self.get_queryset().all().order_by('title')

    def create(self, **kwargs):

        if 'slug' not in kwargs:
            kwargs['slug'] = slugify(kwargs.get('title')) if kwargs.get('title') else None
        return super().create(**kwargs)

class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    ip_address = models.GenericIPAddressField()
    likes_count = models.IntegerField(default=0)

    def __str__(self):
        return f'Like for article "{self.article.title}" by {self.ip_address}'

class Favourite(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='favourites')
    ip_address = models.GenericIPAddressField()
    favourites_count = models.IntegerField(default=0)

    class Meta:
        unique_together = ['article', 'ip_address']

    def __str__(self):
        return f'Favourite for article "{self.article.title}"'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)