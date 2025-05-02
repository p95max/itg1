from django.urls import path
from news.views import (catalog, article_detail, about, news_by_tag,
                        news_by_category, search_news, toggle_like, toggle_favorite,
                        favourites, post_comment, add_article,)
from django.conf import settings
from django.conf.urls.static import static

app_name = 'news'

urlpatterns = [
    path('', catalog, name='catalog'),                                                                # главная страница
    path('article/<slug:slug>/', article_detail, name='article_detail'),                              # статья полностью
    path('news/tag/<str:tag_name>/', news_by_tag, name='news_by_tag'),                                # Новости по тегу
    path('news/category/<str:category_name>/', news_by_category, name='news_by_category'),            # Новости по категории
    path('about/', about, name='about'),                                                              # Страница "О нас"
    path('search/', search_news, name='search_news'),                                                 # форма поиска
    path('toggle_like/<int:article_id>/', toggle_like, name='toggle_like'),                           # лайк под статьей
    path('toggle_favourite/<int:article_id>/', toggle_favorite, name='toggle_favorite'),              # избранное под статьей
    path('favoutires/', favourites, name='favourites'),                                               # избранное стр.
    path('article/<int:article_id>/comment/', post_comment, name='post_comment'),                     # добавить комент
    path('add/', add_article, name='add_article'),                                                    # добавить новую статью

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


