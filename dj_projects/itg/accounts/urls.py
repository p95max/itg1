from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import LoginUser, UserAuthenticationView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='news:catalog'), name='logout'),
    path('auth/', UserAuthenticationView.as_view(), name='registration'),

    ]