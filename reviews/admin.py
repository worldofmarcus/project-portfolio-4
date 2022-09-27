from django.contrib import admin
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')
    list_display = ('title', 'slug', 'category', 'status', 'date_created_on', 'author', 'approved')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'date_created_on')
    actions = ['approve_review', 'publish']

    def approve_review(self, request, queryset):
        queryset.update(approved=True)

    def publish(self, request, queryset):
        queryset.update(status=1)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'date_created_on', 'approved', 'author')
    list_filter = ('approved', 'date_created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)