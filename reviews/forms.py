from django import forms
from django.contrib.auth.models import User
from .models import Comment, Post
from datetime import datetime
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'artist', 'featured_image', 'fragment', 'body', 'category',
                  'release_live_date', 'record_label', 'venue', 'genre', 'rating', 'status',)

        widgets = {
                        'body': SummernoteWidget(),
                        'release_live_date': forms.DateInput(attrs={'type': 'date', 'max': datetime.now().date()}),
                        'record_label': forms.TextInput(attrs={'placeholder': 'If you are reviewing a concert, leave this field blank.'}),
                        'venue': forms.TextInput(attrs={'placeholder': 'If you are reviewing an album, leave this field blank.'}),
                        'category': forms.Select(attrs={'class': 'form-select'}),
                        'genre': forms.Select(attrs={'class': 'form-select'}),
                        'rating': forms.Select(attrs={'class': 'form-select'}),
                        'status': forms.Select(attrs={'class': 'form-select'}),
                        }
        labels = {
            'release_live_date': 'Release Date / Live Date',
        }

