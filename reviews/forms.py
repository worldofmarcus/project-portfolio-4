"""Import relevant modules for the application"""

from datetime import datetime
from allauth.account.forms import SignupForm
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    presentation = forms.CharField(widget=forms.Textarea)
    featured_image = forms.FileField(required=False)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.presentation = self.cleaned_data['presentation']

        # user.featured_image = self.cleaned_data['featured_image']
        user.save()
        return user


class CommentForm(forms.ModelForm):
    """
    This class creates the comment form.
    """

    class Meta:
        """
        This meta class adds the body field to the form
        based on the comment model.
        """

        model = Comment
        fields = ('body',)


class CreateReviewForm(forms.ModelForm):
    """
    This class creates the review form.
    """
    class Meta:
        """
        This meta class adds the fields to the form
        based on the post model. It also adds a number
        of widgets to customize and add functionality
        to the form.
        """

        model = Post
        fields = ('title', 'artist', 'featured_image', 'fragment', 'body',
                  'category', 'release_live_date', 'record_label', 'venue',
                  'genre', 'rating', 'status',)

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
            'featured_image': 'Image [600x600 pixels 1:1]'
        }