from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

from .models import Role

from log_actions.models import LogActions


@receiver(post_save, sender=Role)
def create_role(**kwargs):
    log = LogActions.objects.log_action(date=timezone.now(), role_id=2, action='чёт было', object_id=4, user_id=3)
    if log:
        return log
