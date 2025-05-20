from django.urls import path
from profiles.views import (user_actions)
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user_actions'

urlpatterns = [
    path('user_actions/', user_actions, name='user_actions'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)