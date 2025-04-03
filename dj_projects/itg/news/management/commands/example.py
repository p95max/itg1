from itertools import count
from tkinter.font import names
from unicodedata import category

from django.core.management.base import BaseCommand
from django.db.models import Q, F, Sum, Count, Value, BooleanField, Case, When
from datetime import datetime

from django.template.defaultfilters import title

from news.models import Article, Category, Tag

class Command(BaseCommand):
    help = "Dump serialized to json permissions presets objects into fixtures"

    def handle(self, *args, **kwargs):
        pass
        # category = Category.objects.create(name="Путешествия2")
        # print(category)

        # new_article = Article.objects.create(title="Путешествие в Исландию", content="Исландия — удивительная страна с вулканами и гейзерами.",
        #                                      publication_date="2023-10-15T12:00:00Z", category_id=9, views=100, is_active=True)
        # print(new_article)

        # all_tech_articles = Article.objects.filter(category_id=1)
        # print(all_tech_articles)

        # all_active_articles = Article.objects.filter(is_active=True)
        # print(all_active_articles)

        # update_title = Article.objects.get(id=1)
        # Article.title = "New title"
        # update_title.save()
        # print(Article.title)

        # more_views = Article.objects.filter(id=2).update(views=55)
        # print(more_views)

        # delete_article = Article.objects.get(id=10)
        # delete_article.delete()
        # print(delete_article)

        # new_tag = Tag.objects.create(name="Путешествия2")
        # print(new_tag)

        # article = Article.objects.get(id=21)
        # tag = Tag.objects.get(id='Путешествия')
        # article.tags.add(tag)
        # print(f"{tag.name} added to {article.title}")

        # travel_tag = Tag.objects.get(name='Путешествия')
        # articles = Article.objects.filter(tags=travel_tag)
        # print(articles)

        # tag = Tag.objects.get(name='Путешествия')
        # article = Article.objects.get(id=21)
        # article.tags.remove(tag)
        # print(f"Tag '{tag.name}' was removed from article '{article.title}'")



