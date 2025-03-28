from django.urls import path
from news.views import catalog, all_news, article_detail

urlpatterns = [
    path('', catalog, name='catalog'),                   # /news/ для каталога
    path('all/', all_news, name='all_news'),             # /news/all/ для всех новостей
    path('<int:id>/', article_detail, name='article_detail'),  # /news/<id>/ для деталей
]
