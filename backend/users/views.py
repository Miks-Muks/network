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

from .models import Profile, AddedPhoto, LinksProfile
from .forms import UserCreationForm, AddPhotoForm, LinksForm


# Create your views here.


class ProfileView(View):
    def get(self, request):
        profile = Profile.objects.select_related('user').get(user=request.user)
        added_photo = AddedPhoto.objects.filter(user=request.user)[:3]
        links = LinksProfile.objects.filter(user=request.user)[:3]
        return render(request, 'users/profile.html', {'profile': profile, 'added_photo': added_photo, 'links': links})


def logout_view(request):
    logout(request)
    return redirect('network:index')


class SighInView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/sigin_user.html', {'form': form})

    # @transaction.atomic
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = form.save()
            user = authenticate(request, username=username, password=password)
            profile = Profile.objects.create(user=user)
            return redirect('confirm_email')
        else:
            form = UserCreationForm()
            messeage = 'Форма не валидна'
            return render(request, 'registration/sigin_user.html', {'form': form, 'messeage': messeage})


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
    paginate_by = 8


class AddPhotoView(View):
    def get(self, request):
        form = AddPhotoForm()
        return render(request, 'users/add photo.html', {'form': form})

    def post(self, request):
        form = AddPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            return redirect('users:profile')


class LinksView(View):
    def get(self, request):
        form = LinksForm()
        return render(request, 'users/add links.html', {'form': form})

    def post(self, request):
        form = LinksForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            return redirect('users:profile')
