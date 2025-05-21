from django.shortcuts import render

from news.models import Tag, Category
from user_actions.models import UserAction


def user_action(request):
    user_actions = UserAction.objects.filter(user=request.user)

    all_tags = Tag.objects.all()
    all_categories = Category.objects.all()

    context = {
        'all_tags': all_tags,
        'all_categories': all_categories,
        'user_actions': user_actions,

    }

    return render(request, 'user_action.html', context=context)
