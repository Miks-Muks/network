from django.urls import path, include
import django.contrib.auth.urls

from .views import (
    ProfileView,
    SighInView,
    EditProfile,
    logout_view,
    AddedPhotoView,
    FollowerView,
)

app_name = 'users'
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("sigh in", SighInView.as_view(), name='sign_user'),
    path("profile", ProfileView.as_view(), name='profile'),
    path("edit/<int:pk>", EditProfile.as_view(), name='edit'),
    path("sign out", logout_view, name='log'),
    path("photo", AddedPhotoView.as_view(), name='photo'),
    path("followers", FollowerView.as_view(), name='followers'),

]
