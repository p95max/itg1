from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label = 'Username',
        widget = forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(attrs={'class': 'form-control'}),
    )

class UserRegistrationForm(forms.ModelForm):
    email = forms.CharField(
        label = 'Username',
    )
    password = forms.CharField(
        label = 'Password',
    )
    password2 = forms.CharField(
        label = 'Again password',
    )

    def save(self, commit=True):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError("Passwords don't match")

        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password'])
        user.username = user.email
        user.save()

        return user

    class Meta:

        model = get_user_model()
        fields = ['email', 'password', 'password2']