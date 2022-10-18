"""Import relevant modules for the application"""

from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.utils.text import slugify
from .models import Post, Comment, UserProfile
from .forms import CommentForm, CreateReviewForm, UpdateProfileForm


class HomeView(generic.ListView):
    """
    This class filters out all the objects from the Post model with
    status 1 (published) and approved (true). The result is being ordered
    by date in decreasing order. Template being used is index.html.
    """

    model = Post
    queryset = Post.objects.filter(status=1, approved=True).order_by(
                                   '-date_created_on')
    template_name = 'index.html'
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
    template_name = 'album_reviews.html'
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
    template_name = 'concert_reviews.html'


class MemberReviewView(generic.ListView):
    """
    This class filters out all the objects from the Post model where
    the author is equal to the logged in user. No other filtering
    is being done because the user should see all reviews even if
    they are not approved or published. To achieve this a help method
    is being used (def_queryset). The result is being ordered by date
    in decreasing order. Template being used is member_reviews.html.
    """

    model = Post
    template_name = 'member_reviews.html'
    paginate_by = 6

    def get_queryset(self):
        """
        Help method to filter out author that is logged in user and order it
        by date.
        """

        return Post.objects.filter(author=self.request.user.id).order_by(
                                   '-date_created_on')


class About(generic.TemplateView):
    """
    This class creates a context with all objects from the UserProfile
    model.
    """

    model = UserProfile
    context_object_name = 'user'
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        """
        Help method to filter out all objects from the UserProfile
        model.
        """

        context = super().get_context_data(**kwargs)
        context['profile'] = UserProfile.objects.all()
        return context


class AdminArea(generic.TemplateView):
    """
    This class creates a context based on the models Post, Comment and User.
    This makes all the data in the models accessible in the admin area.
    The queries are being done in the help method get_context_data and are
    based on different filters to get the correct data.
    """

    model = Post
    context_object_name = 'post'
    template_name = 'admin_area.html'

    def get_context_data(self, **kwargs):
        """
        Help method to create contexts and return them to the AdminArea.
        """

        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.all()
        context['comment'] = Comment.objects.all()
        context['reviews_unapproved'] = Post.objects.filter(approved=False)
        context['comments_unapproved'] = Comment.objects.filter(approved=False)
        context['users'] = User.objects.filter(is_active=True)
        return context


def admin_update_status(request, slug):
    """
    This function updates the publish / unpublish value connected
    to the reviews in the admin area.
    """

    post = Post.objects.get(slug=slug)

    if post.status == 0:
        publish = 1
    else:
        publish = 0

    post.status = publish
    post.save()
    return HttpResponseRedirect(reverse('admin_area'))


def admin_update_approval(request, slug):
    """
    This function updates the approve / unapprove value connected
    to the reviews in the admin area.
    """

    post = Post.objects.get(slug=slug)
    if post.approved is True:
        approval = False
    else:
        approval = True

    post.approved = approval
    post.save()
    return HttpResponseRedirect(reverse('admin_area'))


def admin_update_comment(request, pk):
    """
    This function updates the approve / unapprove value connected
    to the comments in the admin area.
    """

    comment = Comment.objects.get(pk=pk)
    if comment.approved is True:
        approval = False
    else:
        approval = True

    comment.approved = approval
    comment.save()
    return HttpResponseRedirect(reverse('admin_area'))


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
        User model and then saves the comment so that it is
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
    model.
    """

    model = Post
    form_class = CreateReviewForm
    template_name = 'create_review.html'
    success_url = '/review/submit-success/'

    def form_valid(self, form):
        """
        Help method to add author and slug to the Post model.
        """

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
        """
        Help method to add author and slug to the Post model.
        """

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
        """
        Help method to get success url
        """

        return self.request.path

    def form_valid(self, form):
        """
        Help method to change the comment to not approved.
        """

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
    success_url = '/review/delete-success/'


class DeleteComment(generic.DeleteView):
    """
    This class handles the deletion of a comment.
    """

    model = Comment
    template_name = 'delete_comment.html'
    success_url = '/comment/delete-success/'


class AdminDeleteReview(generic.DeleteView):
    """
    This class handles the deletion of a review.
    """

    model = Post
    template_name = 'admin_delete_review.html'
    success_url = '/review/admin-delete-success/'


def admin_review_deleted(request):
    """
    A basic function that just returns admin_review.html to be rendered.
    """

    return render(request, 'admin_review_deleted.html')


class AdminDeleteComment(generic.DeleteView):
    """
    This class handles the deletion of a review.
    """

    model = Comment
    template_name = 'admin_delete_comment.html'
    success_url = '/comment/admin-delete-success/'


class UpdateProfile(generic.UpdateView):
    """
    This class handles the creation / updating of profiles. A help method
    has also been implemented to do a user check and validate form.
    table.
    """

    model = UserProfile
    form_class = UpdateProfileForm
    template_name = 'profile_page.html'
    success_url = '/profile/submit-success/'

    def form_valid(self, form):
        """
        A help method to do a user check and validate form.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


def review_submitted(request):
    """
    A basic function that just returns review_submitted.html to be rendered.
    """

    return render(request, 'review_submitted.html')


def review_updated(request):
    """
    A basic function that just returns review_updated.html to be rendered.
    """

    return render(request, 'review_updated.html')


def review_deleted(request):
    """
    A basic function that just returns review_deleted.html to be rendered.
    """

    return render(request, 'review_deleted.html')


def comment_deleted(request):
    """
    A basic function that just returns comment_deleted.html to be rendered.
    """

    return render(request, 'comment_deleted.html')


def profile_submitted(request):
    """
    A basic function that just returns profile_submitted.html to be rendered.
    """

    return render(request, 'profile_submitted.html')


def admin_comment_deleted(request):
    """
    A basic function that just returns admin_comment_deleted.html
    to be rendered.
    """

    return render(request, 'admin_comment_deleted.html')
