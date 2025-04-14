from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls', 'news')),
    path('__debug__/', include('debug_toolbar.urls')),


]