from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    """
    This function tests if the comment body
    field is required.
    """

    def test_comment_body_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')
