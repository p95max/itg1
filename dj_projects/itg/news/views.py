from django.views.generic import ListView, DetailView, TemplateView, CreateView, View
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponseRedirect, request
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from .forms import ArticleForm
import json
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()

        # Комментарии
        context['comments'] = article.comments.order_by('-created_at')

        # Похожие статьи по тегам и категории
        by_tags = Article.objects.filter(tags__in=article.tags.all()).exclude(id=article.id)
        by_category = Article.objects.filter(category=article.category).exclude(id=article.id) if article.category else Article.objects.none()
        context['similar_articles'] = (by_tags | by_category).distinct()[:5]

        # Панель тегов и категорий
        context['all_tags'] = Tag.objects.all()
        context['all_categories'] = Category.objects.all()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = request.POST.get('name')
        text = request.POST.get('text')

        if name and text:
            Comment.objects.create(article=self.object, name=name, text=text)

        return self.get(request, *args, **kwargs)

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

class ToggleFavouriteView(View):
    def post(self, request, article_id):
        if request.headers.get("x-requested-with") != "XMLHttpRequest":
            return HttpResponseBadRequest("Wrong request.")

        article = get_object_or_404(Article, id=article_id)
        ip_address = request.META.get('REMOTE_ADDR')
        liked = False

        existing_favourite = Favourite.objects.filter(article=article, ip_address=ip_address)
        if existing_favourite.exists():
            existing_favourite.delete()
        else:
            Favourite.objects.create(article=article, ip_address=ip_address)
            liked = True

        favourites_count = article.favourites.count()
        return JsonResponse({'favorites_count': favourites_count, 'like': liked})

class FavouritesView(View):
    def get(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        favourites_articles = Favourite.objects.filter(ip_address=ip_address)
        favourites_count = favourites_articles.count()

        all_tags = Tag.objects.all()
        all_categories = Category.objects.all()

        context = {
            'favourites_count': favourites_count,
            'favourites_articles': favourites_articles,
            'all_tags': all_tags,
            'all_categories': all_categories
        }
        return render(request, 'news/favourites.html', context)

    def post(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        article_id = request.POST.get('article_id')

        if article_id:
            favourite_to_remove = Favourite.objects.filter(article_id=article_id, ip_address=ip_address)
            if favourite_to_remove.exists():
                favourite_to_remove.delete()

            favourites_articles = Favourite.objects.filter(ip_address=ip_address)
            favourites_count = favourites_articles.count()

            return redirect('news:favourites')

        return HttpResponseBadRequest('No such article in favourites')

class ResetCommentFlagView(View):
    def post(self, request):
        if 'comment_submitted' in request.session:
            del request.session['comment_submitted']
        return JsonResponse({'status':'success'})









