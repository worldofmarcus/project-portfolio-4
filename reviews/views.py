from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post

class HomeView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1, category='Album').order_by('-date_created_on')
    template_name = ('index.html')
    paginate_by = 6