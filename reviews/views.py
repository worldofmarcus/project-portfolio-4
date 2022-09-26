from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import Post, Comment
from .forms import CommentForm, CreateReviewForm


class HomeView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1, approved=True, category='Album').order_by('-date_created_on')
    template_name = ('index.html')
    paginate_by = 6


class ConcertView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1, approved=True, category='Concert').order_by('-date_created_on')
    template_name = ('concert_reviews.html')
    paginate_by = 6


class MemberReviewView(generic.ListView):
    model = Post
    template_name = ('member_reviews.html')
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user.id).order_by('-date_created_on')


def about(request):
    return render(request, 'about.html')


class DetailView(generic.DetailView):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('date_created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "review_details.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
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


def create_review_view(request):
    if request.POST:
        review_form = CreateReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.slug = slugify(review.title)
            review.author = request.user
            review.save()
        return redirect('home')
    return render(request, 'create_review.html', {'form': CreateReviewForm})


class UpdateReview(generic.UpdateView):
    model = Post
    form_class = CreateReviewForm
    template_name = 'update_review.html'
    success_url = '/member-reviews/'

    def form_valid(self, form):
        form.instance.approved = False
        return super().form_valid(form)


class UpdateComment(generic.UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'update_comment.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.approved = False
        return super().form_valid(form)


class ReviewLike(generic.DetailView):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('review_details', args=[slug]))


class DeleteReview(generic.DeleteView):
    model = Post
    template_name = 'delete_review.html'
    success_url = '/member-reviews/'
