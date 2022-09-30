"""Import relevant modules for the application"""

from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.utils.text import slugify
from .models import Post, Comment
from .forms import CommentForm, CreateReviewForm


class HomeView(generic.ListView):
    """
    This class filters out all the objects from the Post model with
    status 1 (published) and approved (true). The result is being ordered
    by date in decreasing order. Template being used is index.html.
    """

    model = Post
    queryset = Post.objects.filter(status=1, approved=True).order_by(
                                   '-date_created_on')
    template_name = ('index.html')
    paginate_by = 6


class AlbumView(generic.ListView):
    """
    This class filters out all the objects from the Post model with
    status 1 (published), approved (true) and category 'Album'.
    The result is being ordered by date in decreasing order.
    Template being used is album_reviews.html.
    """

    model = Post
    queryset = Post.objects.filter(status=1, approved=True,
                                   category='Album').order_by(
                                   '-date_created_on')
    template_name = ('album_reviews.html')
    paginate_by = 6


class ConcertView(generic.ListView):
    """
    This class filters out all the objects from the Post model with
    status 1 (published), approved (true) and category 'Concert'.
    The result is being ordered by date in decreasing order.
    Template being used is concert_reviews.html.
    """

    model = Post
    queryset = Post.objects.filter(status=1, approved=True,
                                   category='Concert').order_by(
                                   '-date_created_on')
    template_name = ('concert_reviews.html')
    paginate_by = 6


class MemberReviewView(generic.ListView):
    """
    This class filters out all the objects from the Post model where
    the author is the same as the logged in user. No other filtering
    is being done because the user should see all reviews even if
    they are not approved or published. To achieve this a help method
    is being used (def_queryset). The result is being ordered by date
    in decreasing order. Template being used is member_reviews.html.
    """

    model = Post
    template_name = ('member_reviews.html')
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user.id).order_by(
                                   '-date_created_on')


def about(request):
    """
    A basic function that just returns about.html to be rendered.
    """

    return render(request, 'about.html')


def review_submitted(request):
    """
    A basic function that just returns about.html to be rendered.
    """

    return render(request, 'review_submitted.html')

def review_updated(request):
    """
    A basic function that just returns about.html to be rendered.
    """

    return render(request, 'review_updated.html')

class AdminArea(generic.ListView):
    model = Comment
    template_name = ('admin_area.html')

    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     return data


    def get_queryset(self):
        # original qs
        qs = super().get_queryset()
        # filter by a variable captured from url, for example
        print(qs)
        return qs.filter()


class DetailView(generic.DetailView):
    """
    When a user clicks on a review this class handles the detail view
    functionality. It also handles the comment functionality in the
    comment section of each detail view. Template being used is
    review_details.html.
    """

    def get(self, request, slug, *args, **kwargs):
        """
        This function handles the get part of the detail view. It
        filters the query on reviews that are published (status=1).
        It also filters out the approved comments and orders them
        in increasing order. It also runs a check whether or not
        a comment is liked. It then renders the content to
        review_details.html.
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by(
                                        'date_created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            'review_details.html',
            {
                'post': post,
                'comments': comments,
                'liked': liked,
                'commented': False,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug):
        """
        This function handles the post comment part of the detail
        view. It requests the user email and username from the
        user model and then saves the comment so that it is
        connected to the specific user.

        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by(
                                        '-date_created_on')
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
            'review_details.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'comment_form': comment_form,
            },
        )


class CreateReview(generic.CreateView):
    """
    This class handles the creation of new reviews. A help method
    has also been implemented to add author and slug to the Post
    table.
    """

    model = Post
    form_class = CreateReviewForm
    template_name = 'create_review.html'
    success_url = '/review/submit-success/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)



class UpdateReview(generic.UpdateView):
    """
    This class handles the update of of reviews. A help method
    has also been implemented to add author and slug to the Post
    table. The help method also unapproves the review when a user
    has changed it. This means that the review needs a re-approval
    from the administrator before it gets visible for the site
    visitors.
    """

    model = Post
    form_class = CreateReviewForm
    template_name = 'update_review.html'
    success_url = '/review/update-success/'

    def form_valid(self, form):
        form.instance.approved = False
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class UpdateComment(generic.UpdateView):
    """
    This class handles the update of of comments. A help method
    has also been implemented to unapprove the comment when a user
    has changed it. This means that the comment needs a re-approval
    from the administrator before it gets visible for the site
    visitors.
    """

    model = Comment
    form_class = CommentForm
    template_name = 'update_comment.html'

    def get_success_url(self, *args):
        return (self.request.path)


    def form_valid(self, form):
        form.instance.approved = False
        return super().form_valid(form)


class ReviewLike(generic.DetailView):
    """
    This class handles the like functionality on the site with the
    support from a help method.
    """

    def post(self, request, slug):
        """
        This function toggles the like (add/remove) for the
        specific, existing user on the specific review.
        """

        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('review_details', args=[slug]))


class DeleteReview(generic.DeleteView):
    """
    This class handles the deletion of a review.
    """
    model = Post
    template_name = 'delete_review.html'
    success_url = '/member-reviews/'

class DeleteComment(generic.DeleteView):
    """
    This class handles the deletion of a comment.
    """
    model = Comment
    template_name = 'delete_comment.html'
    success_url = '/'
