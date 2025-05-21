from django.contrib import admin
from user_actions.models import UserAction


@admin.register(UserAction)
class UserActionAdmin(admin.ModelAdmin):
    pass
