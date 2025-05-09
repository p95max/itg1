from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from accounts.forms import CustomAuthenticationForm

class LoginUser(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'news/login.html'
    extra_context = {'title': 'Login'}
    redirect_field_name = 'next'

    def get_success_url(self):
        return reverse_lazy('news:catalog')