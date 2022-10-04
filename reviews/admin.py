"""Import relevant modules for the application"""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category, Comment, Genre


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    This class adds fields from the post model to the admin
    area and also add functionality like approve review and
    publish in the action dropdown list.
    """

    summernote_fields = ('body')
    list_display = ('title', 'slug', 'category', 'status', 'date_created_on',
                    'author', 'approved', 'release_live_date',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'date_created_on')
    actions = ['approve_review', 'unapprove', 'publish', 'unpublish']

    def approve_review(self, request, queryset):
        """
        This help method updates the approved field to True
        """

        queryset.update(approved=True)

    def publish(self, request, queryset):
        """
        This help method updates the status field to 1
        """

        queryset.update(status=1)

    def unpublish(self, request, queryset):
        """
        This help method updates the status field to 0
        """

        queryset.update(status=0)

    def unapprove(self, request, queryset):
        """
        This help method updates the status field to 0
        """

        queryset.update(approved=False)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    This class adds fields from the category model to the admin
    area and also add list functionality.
    """

    list_display = ('name', )
    list_filter = ('name', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    This class adds fields from the comment model to the admin
    area and also add functionality like approve comments in the
    action dropdown list.
    """

    list_display = ('name', 'body', 'post', 'date_created_on', 'approved',
                    'author')
    list_filter = ('approved', 'date_created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        This help method updates the approved field to True
        """
        queryset.update(approved=True)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """
    This class adds fields from the category model to the admin
    area and also add list functionality.
    """

    list_display = ('name', )
    list_filter = ('name', )
