from tkinter.font import names

from django.urls import path
from news.views import catalog, all_news, article_detail, about, news_by_tag, article_by_slug

urlpatterns = [
    path('', catalog, name='catalog'),                                                                # Главная страница
    path('news/all/', all_news, name='all_news'),                                                     # Все новости
    path('<int:id>/', article_detail, name='article_detail'),                                         # Детали статьи
    path('news/<slug:slug>', article_by_slug, name='article_by_slug'),
    path('news/tag/<str:tag_name>/', news_by_tag, name='news_by_tag'),                                # Новости по тегу
    path('about/', about, name='about'),                                                              # Страница "О нас"
]


