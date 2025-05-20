from django.contrib.auth import get_user_model
from django.db import models

class UserAction(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    model_name = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    diff = models.JSONField(default=dict)

    def __str__(self):
        return f'{self.created_at}, {self.model_name}, {self.action}'
