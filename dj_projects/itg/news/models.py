from django.db import models
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    content = models.TextField()
    publication_date = models.DateTimeField()
    views = models.IntegerField(default=0)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag", related_name='article')
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class ArticleUserMananger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def sorted_by_abc(self):
        return self.get_queryset().all().order_by('title')

    def create(self, **kwargs):

        if 'slug' not in kwargs:
            kwargs['slug'] = slugify(kwargs.get('title')) if kwargs.get('title') else None
        return super().create(**kwargs)


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name