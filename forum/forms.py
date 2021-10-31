from django.db import models
from django import forms
from .models import ForumPost

class ForumForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['topic', 'description', 'slug']
