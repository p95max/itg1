from django.urls import path
from profiles.views import (user_info, user_articles, user_activities)
from django.conf import settings
from django.conf.urls.static import static

app_name = 'profiles'

urlpatterns = [
    path('user_info/', user_info, name='user_info'),
    path('user_articles/', user_articles, name='user_articles'),
    path('user_activities/', user_activities, name='user_activities'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)