from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publication_date = models.DateTimeField()
    views = models.IntegerField(default=0)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag", related_name='article')

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)