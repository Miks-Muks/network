from django import forms
from .models import CommentTopic, TopicKaif


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentTopic
        fields = ['comment', ]
        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-control'})
        }


class TopicForm(forms.ModelForm):
    class Meta:
        model = TopicKaif
        fields = ['title', 'info', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'info': forms.TextInput(attrs={'class': 'form-control'}),
        }

