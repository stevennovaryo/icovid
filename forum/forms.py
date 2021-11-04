from django.db import models
from django import forms
from .models import *

class ForumForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['topic', 'description', 'slug']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description']