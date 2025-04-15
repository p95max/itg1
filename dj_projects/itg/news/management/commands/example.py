from django.core.management.base import BaseCommand
from django.utils.text import slugify
from news.models import Article

#python manage.py example


class Command(BaseCommand):
    help = "Обновить слаги для всех статей"

    def handle(self, *args, **kwargs):
        pass

        # # Очистка слагов
        # articles = Article.objects.all()
        # for article in articles:
        #     article.slug = ""
        # Article.objects.bulk_update(articles, ['slug'])
        #
        # print(f"{len(articles)} слагов было очищено.")



