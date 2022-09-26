from django import forms
from django.contrib.auth.models import User
from .models import Comment, Post
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'artist', 'featured_image', 'fragment', 'body', 'category',
                  'release_date', 'record_label', 'venue', 'genre', 'rating',)

    body = forms.CharField(widget=SummernoteWidget)


