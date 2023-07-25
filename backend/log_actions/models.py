from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import KaifarikUser, Role


# Create your models here.


class LogManager(models.Manager):
    use_in_migrations = True

    def log_action(self, date: str, user_id: int, action: str, object_id: int | None):
        return self.model.objects.create(
            user_id=user_id,
            date=date,
            object_id=str(object_id),

            action=action,
        )


class LogActions(models.Model):
    date = models.DateTimeField(auto_now=False, verbose_name='Дата и время события')
    user = models.ForeignKey(KaifarikUser, on_delete=models.DO_NOTHING)
    role = models.ManyToManyField(Role, )
    object_id = models.TextField(_('object id'), blank=True, null=True)
    action = models.TextField(verbose_name='Действие')
    objects = LogManager()

    def __str__(self):
        return f'Action by {self.user.username} did: {self.action}'
