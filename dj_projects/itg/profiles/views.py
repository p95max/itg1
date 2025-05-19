from django.contrib.admin.models import LogEntry
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from news.models import Tag, Category, Article
from profiles.forms import ProfileEditForm


def user_info(request):
    username = request.user.username
    all_tags = Tag.objects.all()
    all_categories = Category.objects.all()

    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES)

        if form.is_valid() and not form.errors:
            form.save()

            return HttpResponseRedirect('/profiles/user_info')
    else:
        form = ProfileEditForm()

    context = {
        'form': form,
        'username': username,
        'all_tags': all_tags,
        'all_categories': all_categories,
    }

    return render(request, 'profiles/user_info.html', context=context)

def user_articles(request):
    username = request.user.username
    all_tags = Tag.objects.all()
    all_categories = Category.objects.all()

    user_articles = Article.objects.filter(author_id=request.user.id)
    news_list = Article.objects.filter(is_active=True, author_id=request.user.id)
    paginator = Paginator(news_list, 10)  # 10 статей на страницу

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'username': username,
        'all_tags': all_tags,
        'all_categories': all_categories,
        'user_articles': user_articles,
        'page_obj': page_obj,
    }

    return render(request, 'news/catalog.html', context=context)

def user_activities(request):
    username = request.user.username
    all_tags = Tag.objects.all()
    all_categories = Category.objects.all()

    user_action = LogEntry.objects.filter(user_id=request.user.id)

    context = {
        'username': username,
        'all_tags': all_tags,
        'all_categories': all_categories,
        'user_action': user_action,
    }

    return render(request, 'profiles/user_activities.html', context=context)