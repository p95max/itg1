from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.utils.translation import gettext_lazy as _
from .forms import ArticleForm
import json
from news.models import Article, Tag, Category, Like, Favourite, Comment

def catalog(request):
    sort_by = request.GET.get('sort', 'date')  # сортировка по дате по умол
    sort_options = {
        'date': '-publication_date',
        'views': '-views',
        'likes': '-likes_count',
    }

    sort_field = sort_options.get(sort_by, '-publication_date')

    articles_count = Article.objects.count()
    all_tags = Tag.objects.all()
    all_categories = Category.objects.all()
    likes_count = Like.objects.count()
    favourites_count = Favourite.objects.count()

    news_list = Article.objects.filter(is_active=True).order_by(sort_field)
    paginator = Paginator(news_list, 10)  # 10 статей на страницу

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "articles_count": articles_count,
        "all_tags": all_tags,
        "all_categories": all_categories,
        "page_obj": page_obj,
        "likes_count": likes_count,
        "favourites_count": favourites_count,
        "sort": sort_by,
    }
    return render(request, 'news/catalog.html', context=context)

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    all_tags = Tag.objects.all()
    all_categories = Category.objects.all()
    liked_ips = article.likes.values_list('ip_address', flat=True)
    favourite_ips = article.favourites.values_list('ip_address', flat=True)
    reset_comment_flag(request)

    # Похожие статьи
    similar_articles = Article.objects.filter(
        Q(category=article.category) |
        Q(tags__in=article.tags.all())
    ).exclude(id=article.id).distinct().order_by('-publication_date')[:3]

    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')
        if name and text:
            Comment.objects.create(article=article, name=name, text=text)

    context = {
        "article": article,
        "all_tags": all_tags,
        "all_categories": all_categories,
        "liked_ips": liked_ips,
        "favourite_ips": favourite_ips,
        "similar_articles": similar_articles,
    }

    return render(request, 'news/article_detail.html', context=context)

def about(request):
    all_tags = Tag.objects.all()
    all_categories = Category.objects.all()
    context = {
        'title': _('О нас'),
        'description': _('Мы — команда проекта "Fun news", цель которого — предоставлять актуальные и интересные новости.'),
        'contacts': {
            'email': 'info@fun_news.com',
            'phone': '+8 (888) 888-88-88',
            'address': _('г.Харьков, ул. Академика Павлова, д.10 офис 510'),
        },
        "latitude": 49.9935,  # Харьков
        "longitude": 36.2304,
        "company_name": "Fun news",
        "all_tags": all_tags,
        "all_categories": all_categories,
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
    return render(request, 'news/category_and_tag.html', context)

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
    return render(request, 'news/category_and_tag.html', context)

def search_news(request):
    searched_text = request.GET.get('text')
    articles = []

    if searched_text:
        articles = Article.objects.filter(
            Q(title__icontains=searched_text) | Q(content__icontains=searched_text),
            is_active=True
        )

    paginator = Paginator(articles, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'articles_count': articles.count(),
        'filter': f"Результаты поиска: '{searched_text}'",
        'all_tags': Tag.objects.all(),
        'all_categories': Category.objects.all(),
    }

    return render(request, 'news/catalog.html', context)

@require_POST
@login_required(login_url='account:login')
def toggle_like(request, article_id):
    if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
        ip_address = request.META.get('REMOTE_ADDR')
        article = get_object_or_404(Article, id=article_id)
        liked = False

        existing_like = Like.objects.filter(article=article, ip_address=ip_address)
        if existing_like.exists():
            existing_like.delete()
            article.likes_count -= 1
        else:
            Like.objects.create(article=article, ip_address=ip_address)
            article.likes_count += 1
            liked = True

        article.save()
        return JsonResponse({'likes_count': article.likes_count, 'liked': liked})
    else:
        return HttpResponseBadRequest("Invalid request")

@require_POST
@login_required(login_url='account:login')
def toggle_favorite(request, article_id):
    ip_address = request.META.get('REMOTE_ADDR')
    article = get_object_or_404(Article, id=article_id)
    existing_favourite = Favourite.objects.filter(article=article, ip_address=ip_address)

    if existing_favourite.exists():
        existing_favourite.delete()
        article.favourites_count -= 1
        liked = False
    else:
        Favourite.objects.create(article=article, ip_address=ip_address)
        article.favourites_count += 1
        liked = True

    article.save()

    return JsonResponse({
        'favourites_count': article.favourites_count,
        'liked': liked
    })

@login_required(login_url='account:login')
def favourites(request):
    ip_address = request.META.get('REMOTE_ADDR')
    favourites_articles = Favourite.objects.filter(ip_address=ip_address)
    favourites_articles_count = favourites_articles.count()

    all_tags = Tag.objects.all()
    all_categories = Category.objects.all()

    if request.method == 'POST':
        article_id = request.POST.get('article_id')
        if article_id:
            favourite_to_remove = Favourite.objects.filter(article_id=article_id, ip_address=ip_address)
            if favourite_to_remove.exists():
                favourite_to_remove.delete()
            else:
                return HttpResponseBadRequest("Статья не найдена в избранном.")

        return redirect('news:favourites')

    context = {
        "all_tags": all_tags,
        "all_categories": all_categories,
        'favourites_articles': favourites_articles,
        'favourites_count': favourites_articles_count,
    }

    return render(request, 'news/favourites.html', context)

@require_POST
@login_required(login_url='account:login')
def post_comment(request, article_id):
    if request.method == "POST":
        comment_text = request.POST.get('comment')
        if request.session.get('comment_submitted', False):
            messages.error(request, "Комментарий уже был отправлен.")
            return redirect('news:article', article_id=article_id)
        new_comment = Comment(article_id=article_id, text=comment_text)
        new_comment.save()
        request.session['comment_submitted'] = True
        messages.success(request, "Комментарий успешно отправлен!")
        return redirect('news:article', article_id=article_id)

@login_required(login_url='account:login')
def add_article(request):
    all_tags = Tag.objects.all()
    all_categories = Category.objects.all()

    # Обработка загрузки из JSON
    if request.method == 'POST' and request.FILES.get('json_file'):
        json_file = request.FILES['json_file']
        data = json.load(json_file)
        for article_data in data:
            article = Article(
                title=article_data['title'],
                content=article_data['content'],
                author=request.user
            )
            article.save()
        return HttpResponseRedirect('/news/')

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        category_id = request.POST.get('category')
        tags = request.POST.getlist('tags')

        if not category_id:
            form.add_error('category', 'Выберите категорию.')
        if not tags:
            form.add_error('tags', 'Выберите хотя бы один тег.')

        if form.is_valid() and not form.errors:
            article = form.save(commit=False)
            article.author = request.user
            article.category = Category.objects.get(id=category_id)
            article.save()
            article.tags.set(Tag.objects.filter(id__in=tags))
            return HttpResponseRedirect('/news')
    else:
        form = ArticleForm()

    context = {
        'form': form,
        'all_tags': all_tags,
        'all_categories': all_categories,
    }
    return render(request, 'news/add_article.html', context)

def reset_comment_flag(request):
    if 'comment_submitted' in request.session:
        del request.session['comment_submitted']







