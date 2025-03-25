from unicodedata import category

from django.urls import path
from news.views import get_all_news, get_news_by_id, get_category_by_name


urlpatterns = [
    path('', get_all_news),
    path('<int:news_id>/', get_news_by_id),
    path('<str:slug>/', get_category_by_name)
]