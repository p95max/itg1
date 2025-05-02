from django import forms
from .models import Article, Category, Tag


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content', 'image', 'category', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите контент статьи'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'title': 'Заголовок',
            'content': 'Контент',
            'image': 'Изображение',
            'category': 'Категория',
            'tags': 'Теги'
        }

class ArticleUploadJSONForm(forms.ModelForm):
    json_file = forms.FileField()

    def clean_json_file(self):
        json_file = self.cleaned_data['json_file']
        if not json_file.name.endswith('.json'):
            raise forms.ValidationError('This file is not a JSON file')

        return json_file

    def validate_json_file(self, json_file):
        errors = []
        data = json_file.load(json_file)
        for item in data:
            content = item['content']
            title = item['title']


        return errors
