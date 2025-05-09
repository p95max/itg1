from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label = 'Username',
        widget = forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(attrs={'class': 'form-control'}),
    )

class LoginUser(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'news/login.html'
    extra_context = {'title': 'Login'}
    redirect_field_name = 'next'

    def get_success_url(self):
        return reverse_lazy('news:catalog')