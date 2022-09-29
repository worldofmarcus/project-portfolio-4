"""Import relevant modules for the application"""

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))
RATING_CHOICES = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))


class Category(models.Model):
    """
    This class creates the category model.
    """

    name = models.CharField(max_length=255, unique=True)

    class Meta:
        """
        This meta class orders the model by name.
        """

        ordering = ['name']

    def __str__(self):
        """
        This function returns the name of the category
        to add user readability.
        """

        return str(self.name)


class Genre(models.Model):
    """
    This class creates the genre model.
    """

    name = models.CharField(max_length=255, unique=True)

    class Meta:
        """
        This meta class orders the model by name.
        """
        ordering = ['name']

    def __str__(self):
        """
        This function returns the name of the genre
        to add user readability.
        """

        return str(self.name)


CATEGORY_CHOICES = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in CATEGORY_CHOICES:
    choice_list.append(item)

GENRE_CHOICES = Genre.objects.all().values_list('name', 'name')
genre_list = []
for item in GENRE_CHOICES:
    genre_list.append(item)


class Post(models.Model):
    """
    This class creates the post model.
    """

    title = models.CharField(max_length=255, unique=True)
    artist = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="review_posts")
    featured_image = CloudinaryField('image', default='default_image')
    fragment = models.TextField(blank=True)
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='review_likes',
                                   blank=True)
    category = models.CharField(max_length=255, default='Uncategorized',
                                choices=choice_list)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created_on = models.DateTimeField(auto_now_add=True)
    date_updated_on = models.DateTimeField(auto_now=True)
    release_live_date = models.DateTimeField()
    record_label = models.CharField(max_length=255, blank=True)
    venue = models.CharField(max_length=255, blank=True)
    genre = models.CharField(max_length=255, default='Uncategorized',
                             choices=genre_list)
    rating = models.IntegerField(choices=RATING_CHOICES, default=3)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        This meta class orders the model by date.
        """

        ordering = ['-date_created_on']

    def __str__(self):
        """
        This function returns the title and the name of the author
        to add user readability.
        """

        return self.title + ' || ' + str(self.author)

    def number_of_likes(self):
        """
        This function returns the like count.
        """

        return self.likes.count()


class Comment(models.Model):
    """
    This class creates the comment model.
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="review_comments")
    email = models.EmailField()
    body = models.TextField()
    date_created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        This meta class orders the model by date.
        """

        ordering = ['date_created_on']

    def __str__(self):
        """
        This function returns the body and the name of the author
        to add user readability.
        """

        return self.body + ' || ' + str(self.name)
