from django.shortcuts import render, get_object_or_404
from .models import Article, Tag

def catalog(request):
    articles_count = Article.objects.count()
    news = Article.objects.all().prefetch_related('tags').select_related('category')[:5]
    all_tags = Tag.objects.all()
    context = {
        "articles_count": articles_count,
        'news': news,
        "all_tags": all_tags,
    }
    return render(request, 'news/catalog.html', context=context)

def all_news(request):
    articles_count = Article.objects.count()
    news = Article.objects.all().prefetch_related('tags', 'category')
    all_tags = Tag.objects.all()
    context = {
        "articles_count": articles_count,
        'news': news,
        "all_tags": all_tags,
    }
    return render(request, 'news/all_news.html', context=context)

def article_detail(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return render(request, 'news/error.html', {'message': 'Статья не найдена'})
    return render(request, 'news/article_detail.html', {'article': article})

def about(request):
    context = {
        'title': 'О нас',
        'description': 'Мы — команда проекта "Fun news", цель которого — предоставлять актуальные и интересные новости.',
        'contacts': {
            'email': 'info@fun_news.com',
            'phone': '+8 (888) 888-88-88',
            'address': 'г.Харьков, ул. Академика Павлова, д.10 офис 510',
           },
        "latitude": 49.9935,  # Харьков
        "longitude": 36.2304
    }
    return render(request, 'news/about.html', context=context)

def news_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    news = Article.objects.filter(tags=tag)
    all_tags = Tag.objects.all()
    context = {
        "news": news,
        "articles_count": news.count(),
        "all_tags": all_tags,
        "selected_tag": tag_name
    }
    return render(request, 'news/all_news.html', context)

def article_by_slug(request, slug):
    article = get_object_or_404(Article, slug = slug)
    return render(request, 'news/article_detail.html', {'article': article})
