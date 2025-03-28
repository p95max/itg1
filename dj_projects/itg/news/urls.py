from django.urls import path
from news.views import catalog, article_detail, article_list, total_articles

urlpatterns = [
    path('', catalog),                                                  # main page
    path("articles/", article_list, name="article_list"),               # show all articles
    path("article/<int:id>/", article_detail, name="article_detail"),   # search by id
]
