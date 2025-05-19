from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    username = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username
