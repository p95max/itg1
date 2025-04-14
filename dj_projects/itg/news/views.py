from django.shortcuts import render, get_object_or_404
from .models import Article, Tag, Category

def catalog(request):
    articles_count = Article.objects.count()
    news = Article.objects.all().prefetch_related('tags').select_related('category')[:5]
    all_tags = Tag.objects.all()
    all_categories = Category.objects.all()
    context = {
        "articles_count": articles_count,
        'news': news,
        "all_tags": all_tags,
        "all_categories": all_categories,
    }
    return render(request, 'news/catalog.html', context=context)

def all_news(request):
    articles_count = Article.objects.count()
    news = Article.objects.all().prefetch_related('tags', 'category')
    all_tags = Tag.objects.all()
    all_categories = Category.objects.all()
    context = {
        "articles_count": articles_count,
        'news': news,
        "all_tags": all_tags,
        "all_categories": all_categories,
    }
    return render(request, 'news/all_news.html', context=context)

def article_detail(request, id):
    article = Article.objects.get(id=id)
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
    articles_count = news.count()
    all_categories = Category.objects.all()
    context = {
        "news": news,
        "articles_count": articles_count,
        'filter': f"Тег {tag.name}",
        "all_tags": all_tags,
        "selected_tag": tag_name,
        "all_categories": all_categories,
    }
    return render(request, 'news/by_tag.html', context)

def news_by_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    news = Article.objects.filter(category=category, is_active=True)
    all_tags = Tag.objects.all()
    all_categories = Category.objects.all()
    articles_count = news.count()
    context = {
        'news': news,
        'filter': f"Категория: {category.name}",
        "all_tags": all_tags,
        "all_categories": all_categories,
        "articles_count": articles_count
    }
    return render(request, 'news/by_category.html', context)

def article_by_slug(request, slug):
    article = get_object_or_404(Article, slug = slug)
    return render(request, 'news/article_detail.html', {'article': article})
