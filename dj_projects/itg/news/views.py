from django.shortcuts import render
from .models import Article

def catalog(request):
    articles_count = Article.objects.count()                # articles quantity
    info = {
        "articles_count": articles_count,
    }
    return render(request, 'news/catalog.html', context=info)

def article_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, "news/article_detail.html", {"article": article})

def article_list(request):
    articles = Article.objects.all()
    return render(request, "news/article_list.html", {"articles": articles})

def total_articles(request):
    articles_count = Article.objects.count()
    return render(request, 'news/catalog.html', {"articles_count": articles_count})







