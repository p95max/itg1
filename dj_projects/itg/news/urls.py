from django.urls import path
from news.views import (GetAllNewsView, ArticleDetailView, about, news_by_tag,
                        news_by_category, search_news, toggle_like, toggle_favorite,
                        favourites, post_comment, add_article,)
from django.conf import settings
from django.conf.urls.static import static

app_name = 'news'

urlpatterns = [
    path('', GetAllNewsView.as_view(), name='catalog'),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('news/tag/<str:tag_name>/', news_by_tag, name='news_by_tag'),
    path('news/category/<str:category_name>/', news_by_category, name='news_by_category'),
    path('about/', about, name='about'),
    path('search/', search_news, name='search_news'),
    path('toggle_like/<int:article_id>/', toggle_like, name='toggle_like'),
    path('toggle_favourite/<int:article_id>/', toggle_favorite, name='toggle_favorite'),
    path('favoutires/', favourites, name='favourites'),
    path('article/<int:article_id>/comment/', post_comment, name='post_comment'),
    path('add/', add_article, name='add_article'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


