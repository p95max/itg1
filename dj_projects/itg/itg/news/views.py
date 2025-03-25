from django.http import HttpResponse
from django.shortcuts import render


def get_all_news(request):
    info = {
        'news_count': 100600,
        'users_count': 1000,
        'menu': ['Главная', 'О проекте', 'Каталог'],

    }
    return render(request, 'news/catalog.html')

def get_news_by_id(request, news_id):
    return HttpResponse(f"Новость {news_id}")


