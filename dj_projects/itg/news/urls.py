from unicodedata import category

from django.urls import path
from news.views import get_all_news, get_news_by_id, get_category_by_name, main, article_detail, article_list

urlpatterns = [
    path('', get_all_news),
    path("articles/", article_list, name="article_list"),
    path("article/<int:id>/", article_detail, name="article_detail"),  # Добавьте этот путь
]
