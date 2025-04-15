from tkinter.font import names

from django.urls import path
from news.views import (catalog, article_detail, about, news_by_tag,
                        article_by_slug, news_by_category, search_news)

app_name = 'news'

urlpatterns = [
    path('', catalog, name='catalog'),
    path('article/<slug:slug>/', article_detail, name='article_detail'),
    # path('<int:id>/', article_detail, name='article_detail'),
    path('news/tag/<str:tag_name>/', news_by_tag, name='news_by_tag'),                                # Новости по тегу
    path('news/category/<str:category_name>/', news_by_category, name='news_by_category'),            # Новости по категории
    path('about/', about, name='about'),                                                              # Страница "О нас"
    path('search/', search_news, name='search_news'),                                                 # форма поиска
]


