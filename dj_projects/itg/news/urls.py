from tkinter.font import names

from django.urls import path
from news.views import catalog, all_news, article_detail, about_us

urlpatterns = [
    path('', catalog, name='catalog'),
    path('all/', all_news, name='all_news'),
    path('<int:id>/', article_detail, name='article_detail'),
    path('about/', about_us, name='about_us')
]
