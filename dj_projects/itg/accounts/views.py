from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomAuthenticationForm, UserRegistrationForm


class LoginUser(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'news/custom_auth/login.html'
    extra_context = {'title': 'Login'}
    redirect_field_name = 'next'

    def get_success_url(self):
        return reverse_lazy('news:catalog')

class UserAuthenticationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'news/custom_auth/auth.html'

    def get_success_url(self):
        return reverse_lazy('news:catalog')

