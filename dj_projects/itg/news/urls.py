from django.urls import path
from news.views import catalog, article_detail, get_all_news, total_articles

urlpatterns = [
    path('', catalog),                                                                                                  # main page
    path("articles/", get_all_news, name="news_list"),                                                               # show all articles
    path("article/<int:id>/", article_detail, name="article_detail"),                                                   # search by id

]
