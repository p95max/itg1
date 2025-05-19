from django import forms
from profiles.models import Profile
from django.utils.translation import gettext_lazy as _

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'avatar']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Введите ваше имя') }),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': _('Имя'),
            'avatar': _('Аватар'),
        }