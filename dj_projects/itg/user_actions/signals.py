from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from news.models import Article, Category, Tag
from user_actions.middlewares import get_current_user
from user_actions.models import UserAction


def diff_model(new, old):
    new_data = new.__dict__
    old_data = old.__dict__

    keys = []

    for key in new_data.keys():
        keys.append(key)
    for key in old_data.keys():
        keys.append(key)

    keys = list(set(keys))
    diff = {}
    for key in keys:
        old_value = old_data.get(key)
        new_value = new_data.get(key)

        if old_value != new_value:
            diff[key] = {'old': old_value, 'new': new_value}
    return diff

def changes(sender, instance, **kwargs):
    if kwargs.get("raw", False):
        return

    id = getattr(instance, 'id', None)
    if id:
        try:
            old_value = sender.objects.get(id=id)
            diff = diff_model(instance, old_value)
            action = 'change'
        except sender.DoesNotExist:
            action = 'add'
            diff = {}
    else:
        action = 'add'
        diff = {}

    UserAction.objects.create(
        action=action,
        diff=diff,
        model_name=instance._meta.model_name,
        user=get_current_user()
    )

def delete(sender, instance, **kwargs):
    if kwargs.get("raw", False):
        return

    UserAction.objects.create(
        action='delete',
        diff={},
        model_name=instance._meta.model_name,
        user=get_current_user()
    )




pre_save.connect(changes, sender=Article)
pre_save.connect(changes, sender=Category)
pre_save.connect(changes, sender=Tag)
