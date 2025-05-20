from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from news.models import Article, Category, Tag
from user_actions.models import UserAction


def diff_model(new, old):
    new_data = new.__dict__()
    old_data = old.__dict__()

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

@receiver(pre_save, sender=(Article, Category, Tag) )
def changes(sender, instance, **kwargs):
    id = getattr(instance, 'id', None)
    if id:
        old_value = instance.__model__.objects.get(id=id)
        diff = diff_model(instance, old_value)

        action = 'change'
    else:
        action = 'add'
        diff = {}

    UserAction.objects.create(action=action,diff=diff, model_name=instance.__model__.__name__)

@receiver(post_delete, sender=(Article, Category, Tag) )
def delete(sender, instance, **kwargs):
    UserAction.objects.create(action='delete', diff={}, model_name=instance.__model__.__name__)