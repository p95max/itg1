import importlib

from django.apps import AppConfig


class UserActionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_actions'

    def ready(self):
        importlib.import_module("user_actions.signals")
