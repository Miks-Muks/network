from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import LogActions


# Create your views here.


class ActionsList(LoginRequiredMixin, View):

    def get(self, request):
        actions = LogActions.objects.all()
        return render(request, 'log_actions/list.html', {'actions': actions})
