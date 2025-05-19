from django.contrib import admin
from django.contrib.admin import SimpleListFilter, FieldListFilter
from django.core.exceptions import PermissionDenied

from profiles.models import Profile
from .models import Article, Category, Tag

class ArticleSpiderFilter(FieldListFilter):
    title = 'Внутри пауки'
    parameter_name = 'title'

    def lookups(self, request, model_admin):
        return [
            ('spiders', 'пауки'),
            ('no spiders', 'нет пауков')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'spiders':
            return queryset.filter(title__contains='пауки')
        if self.value() == 'no spiders':
            return queryset.all()
        return queryset

def make_inactive(self, modeladmin, request, queryset):
    if not request.user.has_perm('news.make_active'):
        raise PermissionDenied('Permission denied')
    if queryset:
        queryset.update(is_active=False)
    make_inactive.short_description = 'Сделать неактивными выбранные статьи'

class TagInline(admin.TabularInline):
    model = Article.tags.through
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'publication_date', 'views', 'is_active')
    list_filter = ('category', 'is_active',)
    list_per_page = 15                                                                      #кон-во статей на стр
    list_display_links = ('id',)                                                            #ссылка на поле
    search_fields = ('title', 'content')
    fields = ('title', 'content', 'category', 'tags', 'is_active')
    ordering = ('-views',)                                                                  #сортировка по
    readonly_fields = ('views',)
    list_editable = ('title', 'category',)
    actions_on_top = True
    save_as = True

    inlines = [TagInline]
    actions = [make_inactive]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass




