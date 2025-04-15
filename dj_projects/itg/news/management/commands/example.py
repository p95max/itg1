from django.core.management.base import BaseCommand
from django.utils.text import slugify
from news.models import Article

#python manage.py example


class Command(BaseCommand):
    help = "Обновить слаги для всех статей"

    def handle(self, *args, **kwargs):
        def unique_slugify(title, instance_id=None):
            base_slug = slugify(title)
            slug = base_slug
            num = 1
            while Article.objects.exclude(id=instance_id).filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            return slug

        # # Очистка слагов
        # articles = Article.objects.all()
        # for article in articles:
        #     article.slug = ""
        # Article.objects.bulk_update(articles, ['slug'])
        #
        # print(f"{len(articles)} слагов было очищено.")



