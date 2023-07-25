from django.urls import path

from .views import ActionsList

app_name = 'actions'
urlpatterns = [
    path('list', ActionsList.as_view(), name='list')
]
