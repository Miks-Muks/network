from django.shortcuts import render, redirect
from django.views.generic import (
    View,
    UpdateView,
    ListView,
    DetailView,
)
from django.contrib.auth import logout, authenticate
from django.db import transaction
from django.contrib.auth import login

from .models import Profile, AddedPhoto
from .forms import CreateUserForm, ProfileForm


# Create your views here.


class ProfileView(View):
    def get(self, request):
        profile = Profile.objects.select_related('user').get(user=request.user)
        added_photo = AddedPhoto.objects.filter(user=request.user)[:3]
        return render(request, 'users/profile.html', {'profile': profile, 'added_photo': added_photo})


def logout_view(request):
    logout(request)
    return redirect('network:index')


class SighInView(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, 'users/login_user.html', {'form': form})

    # @transaction.atomic
    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            return redirect('/')
        else:
            result = form.is_valid()
            return render(request, 'users/login_user.html', {'result': result})


class EditProfile(UpdateView):
    model = Profile
    template_name = 'users/edit.html'
    fields = ['about', 'city', 'photo']
    success_url = '/users/profile'


class AddedPhotoView(ListView):
    model = AddedPhoto
    template_name = 'users/added_photo.html'
    paginate_by = 10
    context_object_name = 'photo'


class FollowerView(ListView):
    template_name = 'network/followers.html'
    queryset = Profile.objects.all()
    context_object_name = 'follower'
