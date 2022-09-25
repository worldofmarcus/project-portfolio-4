from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'artist', 'featured_image', 'fragment', 'body', 'category',
                  'release_date', 'record_label', 'venue', 'genre', 'rating',)

