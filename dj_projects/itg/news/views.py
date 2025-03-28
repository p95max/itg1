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










