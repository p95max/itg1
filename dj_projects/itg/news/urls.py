from django.urls import path
from news.views import catalog

urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('catalog/<int:id>/', catalog, name='article_detail'),
]
