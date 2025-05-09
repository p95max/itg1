from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import Q
from django.utils.text import slugify
from django.utils import timezone

class ArticleQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

    def by_category(self, category_id):
        return self.active().filter(category_id=category_id)

    def by_tag(self, tag_id):
        return self.active().filter(tags__id=tag_id)

    def search(self, query):
        return self.active().filter(Q(title__icontains=query) | Q(description__icontains=query))

    def sorted(self, sort_by='publication_date', order='desc'):
        valid_sort_field = {'publication_date': 'views',}
        if sort_by not in valid_sort_field:
            sort = 'publication_date'
        order_by = f'-{sort_by}' if order == 'desc' else sort
        return self.active().order_by(order_by)

class ArticleUserMananger(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def sorted(self, sort, order):
        return self.get_queryset().sorted(sort, order)

    def create(self, **kwargs):
        if 'slug' not in kwargs:
            kwargs['slug'] = slugify(kwargs.get('title')) if kwargs.get('title') else None
        return super().create(**kwargs)

    def by_tag(self, tag_id):
        return self.get_queryset().by_tag(tag_id)

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    publication_date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name='Категория', blank=True,
                              null=True)
    tags = models.ManyToManyField("Tag", related_name='article',  verbose_name='Теги', blank=True,
                              null=True)
    likes_count = models.IntegerField(default=0)
    favourites_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True,  verbose_name='Теги')
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='articles/%Y/%m/%d/',
                              validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'jpeg'])],
                              blank=True,
                              null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True,
                               default=None, verbose_name='Author')

    objects = ArticleUserMananger()

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




