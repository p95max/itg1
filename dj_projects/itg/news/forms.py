from django import forms

from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(
        label='Заголовок',
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите заголовок'
        })
    )

    content = forms.CharField(
        label='Текст статьи',
        max_length=1000,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 6,
            'placeholder': 'Введите текст статьи'
        })
    )

