from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('account/', include('allauth.urls')),
    # path('auth/', include('accounts.urls')),  custom auth/login
    path('profiles/', include('profiles.urls')),
    path('user_actions/', include('user_actions.urls')),
]

urlpatterns += i18n_patterns(
    path('news/', include('news.urls', namespace='news')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
