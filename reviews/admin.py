from django.contrib import admin
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')
    list_display = ('title', 'slug', 'category', 'status', 'date_created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'date_created_on')