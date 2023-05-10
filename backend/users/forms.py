from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'about', 'photo']
        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'about': forms.TextInput(attrs={'class': 'form-control'}),
        }