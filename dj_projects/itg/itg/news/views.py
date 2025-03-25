from django.http import HttpResponse
from django.shortcuts import render


def get_all_news(request):
    info = {
        "users_count": 100600,
        "news_count": 100600,
        "menu": [
            {"title": "Главная",
             "url": "/",
             "url_name": "index"},
            {"title": "О проекте",
             "url": "/about/",
             "url_name": "about"},
            {"title": "Каталог",
             "url": "/news/catalog/",
             "url_name": "catalog"},
        ]
    }
    return render(request, 'news/catalog.html', context=info)

def get_news_by_id(request, news_id):
    return HttpResponse(f"Новость {news_id}")

def get_category_by_name(request, slug):
    return HttpResponse(f"Категория {slug}")


