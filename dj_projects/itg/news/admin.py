from django.contrib import admin

from .models import Article, Category, Tag

def make_inactive(modeladmin, request, queryset):
    if queryset:
        queryset.update(is_active=False)
        make_inactive.short_description = 'Сделать неактивными выбранные статьи'

class TagInline(admin.TabularInline):
    model = Article.tags.through
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publication_date', 'views', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'content')
    fields = ('title', 'content', 'category', 'tags', 'is_active')
    ordering = ('-publication_date',)
    inlines = [TagInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass