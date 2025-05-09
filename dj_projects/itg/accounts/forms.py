from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import gettext_lazy as _

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label = _('Введите логин:'),
        widget = forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        label = _('Введите пароль:'),
        widget = forms.PasswordInput(attrs={'class': 'form-control'}),
    )

class UserRegistrationForm(forms.ModelForm):
    email = forms.CharField(
        label=_('Введите ваш Email:'),
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label=_('Введите ваш пароль:'),
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label=_('Введите ваш пароль еще раз:'),
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def save(self, commit=True):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError(_('Пароли не совпадают!'))
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password'])
        user.username = user.email
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'password2']