from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Profile, AddedPhoto, LinksProfile

KaifarikUser = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(UserCreationForm.Meta):
        model = KaifarikUser
        fields = ("username", "email")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'about', 'photo']
        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'about': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = AddedPhoto
        fields = ['image', 'description']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class LinksForm(forms.ModelForm):
    class Meta:
        model = LinksProfile
        fields = ['link']
        widgets = {
            'link': forms.URLInput(attrs={"class": "form-control"}),
        }
        labels = {
            'link': 'Url adress'
        }
