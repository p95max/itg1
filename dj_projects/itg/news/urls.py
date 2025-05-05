from django.urls import path
from news.views import (GetAllNewsView, ArticleDetailView, AboutUsView, ArticleFilterView, SearchArticleView, ToggleLikeView, ToggleFavouriteView,
                        FavouritesView, PostCommentView, CreateArticleView, ResetCommentFlagView)
from django.conf import settings
from django.conf.urls.static import static

app_name = 'news'

urlpatterns = [
    path('', GetAllNewsView.as_view(), name='catalog'),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('news/<str:filter_type>/<str:name>/', ArticleFilterView.as_view(), name='filtered_news'),
    path('about/', AboutUsView.as_view(), name='about'),
    path('search/', SearchArticleView.as_view(), name='search_news'),
    path('toggle_like/<int:article_id>/', ToggleLikeView.as_view(), name='toggle_like'),
    path('toggle_favourite/<int:article_id>/', ToggleFavouriteView.as_view(), name='toggle_favorite'),
    path('favoutires/', FavouritesView.as_view(), name='favourites'),
    path('article/<int:article_id>/comment/', PostCommentView.as_view(), name='post_comment'),
    path('add/', CreateArticleView.as_view(), name='add_article'),
    path('reset_comment_flag/', ResetCommentFlagView.as_view(), name='reset_comment_flag'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


