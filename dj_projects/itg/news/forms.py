from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(label='Введите заглавие: ', max_length=255)
    content = forms.CharField(label='Введите текст статье :', widget=forms.Textarea, max_length=1000)
