from django.shortcuts import render
from .models import Article

def catalog(request):
    articles_count = Article.objects.count()
    news = Article.objects.all().prefetch_related('tags', 'category')[:3]
    context = {
        "articles_count": articles_count,
        'news': news,
    }
    return render(request, 'news/catalog.html', context=context)

def all_news(request):
    articles_count = Article.objects.count()
    news = Article.objects.all().prefetch_related('tags', 'category')
    context = {
        "articles_count": articles_count,
        'news': news,
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












