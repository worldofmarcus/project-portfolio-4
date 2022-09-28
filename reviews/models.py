from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))
RATING_CHOICES = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
GENRE = ((0, 'Electronic'), (2, 'Folk/Country'), (3, 'Jazz'), (4, 'Pop/R&B'),
         (5, 'Rock'), (6, 'Experimental'), (7, 'Global'), (8, 'Metal'),
         (9, 'Rap/Hip-Hop'), (10, 'Uncategorized'))


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)


CATEGORY_CHOICES = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in CATEGORY_CHOICES:
    choice_list.append(item)


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    artist = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="review_posts")
    featured_image = CloudinaryField('image', default='default_image')
    fragment = models.TextField(blank=True)
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='review_likes', blank=True)
    category = models.CharField(max_length=255, default='Uncategorized', choices=choice_list)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created_on = models.DateTimeField(auto_now_add=True)
    date_updated_on = models.DateTimeField(auto_now=True)
    release_live_date = models.DateTimeField()
    record_label = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    genre = models.IntegerField(choices=GENRE, default=10)
    rating = models.IntegerField(choices=RATING_CHOICES, default=3)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_created_on']

    def __str__(self):
        return self.title + ' || ' + str(self.author)

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="review_comments")
    email = models.EmailField()
    body = models.TextField()
    date_created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_created_on']

    def __str__(self):
        return self.body + ' || ' + str(self.name)
