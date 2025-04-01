from itertools import count
from unicodedata import category

from django.core.management.base import BaseCommand
from django.db.models import Q, F, Sum, Count, Value, BooleanField, Case, When
from datetime import datetime
from news.models import Article, Category, Tag

class Command(BaseCommand):
    help = "Dump serialized to json permissions presets objects into fixtures"

    def handle(self, *args, **kwargs):
        pass

        # date_test = datetime.now()
        # articles = Article.objects.annotate(
        #     is_featured=Case(
        #         When(publication_date__gt=date_test, then=Value(True)),
        #         default=Value(False),
        #         output_field=BooleanField(),
        #     )
        # ).query

        # print(
        #     Article.objects.filter(publication_date__gt=date_test)
        #     Article.objects.filter(Q(category__name="Образование") | Q(tags__name="Инновации")).exists()
        #     Article.objects.filter(~Q(category__name="Культура"))
        #     Article.objects.filter(Q(category__name="Здоровье") | Q(category__name="Образование") & Q(tags__name="Исследования") )
        #     Article.objects.all().update(views=F('views') +1 )
        #     Article.objects.filter(publication_date__year=2023).count()
        #     Article.objects.filter(Q(category__name="Технологии") & Q(tags__name="Инновации"))
        #     Article.objects.values("category__name").annotate(total_articles=Count(F('pk')))
        #     Article.objects.aggregate(total_views=Sum("views"))
        #     Article.objects.filter(views__gt=1)
        # )
        # print(str(articles))

