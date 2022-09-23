from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post

class HomeView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1, category='Album').order_by('-date_created_on')
    template_name = ('index.html')
    paginate_by = 6

class ConcertView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1, category='Concert').order_by('-date_created_on')
    template_name = ('concert_reviews.html')
    paginate_by = 6

def about(request):
    return render(request, 'about.html')

class DetailView(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('date_created_on')
        return render(
            request,
            "review_details.html",
            {
                "post": post,
                "comments": comments,
            },
        )
