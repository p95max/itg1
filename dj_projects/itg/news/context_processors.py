from django.core.cache import cache
from news.models import Article, Category, Favourite, Like, Tag

def global_settings(request):

    if cache.get('favourite_count') is None:
        cache.set('favourite_count', Favourite.objects.count(), 60 * 15)
    if cache.get('like_count') is None:
        cache.set('like_count', Like.objects.count(), 60 * 15)
    if cache.get('articles_count') is None:
        cache.set('articles_count', Article.objects.count(), 60 * 15)
    if cache.get('all_tags_count') is None:
        cache.set('all_tags_count', Tag.objects.count(), 60 * 15)
    if cache.get('all_categories_count') is None:
        cache.set('all_categories_count', Category.objects.count(), 60 * 15)

    return {
        'favourites_count': cache.get('favourite_count'),
        'likes_count': cache.get('like_count'),
        'articles_count': cache.get('articles_count'),
        'all_tags': cache.get('all_tags_count'),
        'all_categories': cache.get('all_categories_count'),
    }