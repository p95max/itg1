from ipaddress import ip_address

from django.views.generic import ListView, DetailView, TemplateView, CreateView, View
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponseRedirect, request
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import ArticleForm
import json
import requests
from news.models import Article, Tag, Category, Like, Favourite, Comment

class GetAllNewsView(ListView):
    model = Article
    template_name = 'news/catalog.html'
    context_object_name = 'news'
    paginate_by = 20

    def get_queryset(self):
        order_by = self.request.GET.get('order_by', '-publication_date')
        return Article.objects.select_related('category').prefetch_related('tags').order_by(order_by)

    def get_context_data(self, **kwargs):
        context = super(GetAllNewsView, self).get_context_data(**kwargs)

        articles_count = Article.objects.count()
        all_tags = Tag.objects.all()
        all_categories = Category.objects.all()
        likes_count = Like.objects.count()
        favourites_count = Favourite.objects.count()

        context.update({
            "articles_count": articles_count,
            "all_tags": all_tags,
            "all_categories": all_categories,
            "likes_count": likes_count,
            "favourites_count": favourites_count,
        })
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'news/article_detail.html'
    context_object_name = 'article'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views += 1
        self.object.save()

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = request.POST['name']
        text = request.POST['text']

        if name in text:
            Comment.objects.create(article=self.object, text=text)
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()

        # Simular articles
        similar_articles = Article.objects.filter(
            Q(category=article.category) |
            Q(tags__in=article.tags.all())
        ).exclude(id=article.id).distinct().order_by('-publication_date')[:3]

        # Likes and favourites
        liked_ips = article.likes.values_list('ip_address', flat=True)
        favourite_ips = article.favourites.values_list('ip_address', flat=True)

        context.update({
                    "all_tags": Tag.objects.all(),
                    "all_categories": Category.objects.all(),
                    "liked_ips": liked_ips,
                    "favourite_ips": favourite_ips,
                    "similar_articles": similar_articles,
        })
        return context

class AboutUsView(TemplateView):
    template_name = 'news/about.html'

    all_tags = Tag.objects.all()
    all_categories = Category.objects.all()

    extra_context = {
        'title': 'О нас',
        'description': 'Мы — команда проекта "Fun news", цель которого — предоставлять актуальные и интересные новости.',
        'contacts': {
            'email': 'info@fun_news.com',
            'phone': '+8 (888) 888-88-88',
            'address': 'г.Харьков, ул. Академика Павлова, д.10 офис 510',
        },
        "latitude": 49.9935,  # Харьков
        "longitude": 36.2304,
        "company_name": "Fun news",
        "all_tags": all_tags,
        "all_categories": all_categories,
    }

class CreateArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'news/add_article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_categories'] = Category.objects.all()
        context['all_tags'] = Tag.objects.all()
        return context

    def post(self, request, *args, **kwargs):

        if request.FILES.get('json_file'):
            json_file = request.FILES['json_file']
            try:
                data = json.load(json_file)
            except json.JSONDecodeError:
                form = self.get_form()
                form.add_error(None, ("Неверный формат JSON-файла"))
                return self.form_invalid(form)

            for item in data:
                # Загружаем статью из JSON
                article = Article(
                    title=item['title'],
                    content=item['content'],
                    category=Category.objects.get(id=item['category_id'])
                )
                article.save()
                if 'tags_ids' in item:
                    article.tags.set(Tag.objects.filter(id__in=item['tags_ids']))

            return redirect('news:catalog')

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        article = form.save()
        return redirect('news:article_detail', slug=article.slug)

class PostCommentView(View):
    def post(self, request, article_id):
        commnent_text = request.POST['comment']
        if request.session.get('comment_submitted', False):
            messages.error(request, 'Comment already submitted')
        else:
            Comment.objects.create(article_id = article_id, text = commnent_text)
            request.session['comment_submitted'] = True
            messages.success(request, 'Comment submitted')
        return redirect('news:article_detail', article_id=article_id)

class ArticleFilterView(ListView):
    model = Article
    template_name = 'news/category_and_tag.html'
    context_object_name = 'articles'
    paginate_by = 20

    def get_queryset(self):
        self.filter_type = self.kwargs.get('filter_type')
        self.name = self.kwargs.get('name')

        if self.filter_type == 'tag':
            self.filter_object = get_object_or_404(Tag, name=self.name)
            return Article.objects.filter(tags = self.filter_object, is_active=True)
        elif self.filter_type == 'category':
            self.filter_object = get_object_or_404(Category, name=self.name)
            return Article.objects.filter(category = self.filter_object, is_active=True)
        else:
            return Article.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles_count'] = self.object_list.count()
        context['filter'] = f"{'Tag' if self.filter_type == 'tag' else 'Category'}: {self.name}"
        context['all_tags'] = Tag.objects.all()
        context['all_categories'] = Category.objects.all()
        if self.filter_type == 'tag':
            context['selected_tag'] = self.name
        return context

class SearchArticleView(ListView):
    model = Article
    template_name = 'news/catalog.html'
    context_object_name = 'page_obj'
    paginate_by = 20

    def get_queryset(self):
        searched_text = self.request.GET.get('text')
        if searched_text:
            return Article.objects.filter(
                Q(title__icontains=searched_text) | Q(content__icontains=searched_text),
                is_active=True
            )
        return Article.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        searched_text = self.request.GET.get('text', '')
        context.update({
            'articles_count': self.get_queryset().count(),
            'filter': f"Результаты поиска: '{searched_text}'",
            'all_tags': Tag.objects.all(),
            'all_categories': Category.objects.all()
        })
        return context

class ToggleLikeView(View):
    def post(self, request, article_id):
        if request.headers.get("x-requested-with") != "XMLHttpRequest":
            return HttpResponseBadRequest("Wrong request.")

        article = get_object_or_404(Article, id=article_id)
        ip_address = request.META.get('REMOTE_ADDR')
        liked = False

        existing_like = Like.objects.filter(article=article, ip_address=ip_address)
        if existing_like.exists():
            existing_like.delete()
        else:
            Like.objects.create(article=article, ip_address=ip_address)
            liked = True

        likes_count = article.likes.count()
        return JsonResponse({'likes_count': likes_count, 'like': liked})


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

def reset_comment_flag(request):
    if 'comment_submitted' in request.session:
        del request.session['comment_submitted']









