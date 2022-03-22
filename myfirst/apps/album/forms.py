from .models import Track, Text, Album
from django.forms import ModelForm, TextInput, Textarea


class TrackForm(ModelForm):
    class Meta:
        track = Track
        fields = ['track']
        widgets = {
            'track': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Название трека'
            }),
        }


class TextForm(ModelForm):
    class Meta:
        text = Text
        fields = ['text']
        widgets = {
            'text': Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Текст трека'
            })
        }
