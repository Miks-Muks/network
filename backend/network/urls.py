from django.urls import path
from .views import IndexView, TopicsView, TopicDetail, TopicCreate, CommentCreate, CheckView

app_name = 'network'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('check', CheckView.as_view(), name='check'),
    path('topics', TopicsView.as_view(), name='topics'),
    path('topics/<int:pk>', TopicDetail.as_view(), name='detail'),
    path('topics/create', TopicCreate.as_view(), name='create'),
    path('comment_create/<int:pk_topic>', CommentCreate.as_view(), name='comment_create'),
]
