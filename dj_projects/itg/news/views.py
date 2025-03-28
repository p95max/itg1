from django.shortcuts import render
from .models import Article

def catalog(request, id=None):
    if id is None:
        articles_count = Article.objects.count()
        news = Article.objects.all().prefetch_related('tags', 'category')
        context = {
            "articles_count": articles_count,
            'news': news,
        }
        return render(request, 'news/catalog.html', context=context)
    else:
        try:
            article = Article.objects.get(id=id)
        except Article.DoesNotExist:
            return render(request, 'news/error.html', {'message': 'Статья не найдена'})
        return render(request, 'news/article_detail.html', {'article': article})











