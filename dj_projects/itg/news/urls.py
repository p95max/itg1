from django.urls import path
from news.views import catalog, all_news, article_detail, about

urlpatterns = [
    path('', catalog, name='catalog'),
    path('all/', all_news, name='all_news'),
    path('<int:id>/', article_detail, name='article_detail'),
    path('about/', about, name='about'),
]
