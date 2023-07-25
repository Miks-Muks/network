from abc import ABC, abstractmethod

from .models import LogActions

from users.models import Role
from django.utils import timezone


class BaseActionsCreator(ABC):

    def __init__(self, ):
        pass

    @abstractmethod
    def create(self):
        pass


class ActionsCreatorPost(BaseActionsCreator):

    def create(self, request):
        user_role = Role.objects.get(pk=request.user.id)
        user = request.user.id
        action = request.POST.get('title')

        log = LogActions.objects.log_action(date=timezone.now(), action=f'Написал пост с таким сожержанием {action}',
                                            user_id=user,
                                            object_id=1)
        log.role.add(user_role.id)
