from django import forms
from .models import Article, Category, Tag

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content','image', 'category', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите контент статьи'}),
            'publication_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),  # Поле выбора категории
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'})  # Поле выбора тегов
        }
        labels = {
            'title': 'Заголовок',
            'content': 'Контент',
            'publication_date': 'Дата публикации',
            'image': 'Изображение',
            'category': 'Категория',
            'tags': 'Теги'
        }
