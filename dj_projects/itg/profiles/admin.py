from django.contrib import admin
from profiles.models import Profile


@admin.register(Profile)
class ProfileUser(admin.ModelAdmin):
    pass
