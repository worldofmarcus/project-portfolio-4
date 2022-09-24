from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import CommentForm


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

class MemberReviewView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-date_created_on')
    template_name = ('member_reviews.html')

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user.id)



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
                "commented": False,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-date_created_on")

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "review_details.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,

            },
        )
