from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('concert-reviews/', views.ConcertView.as_view(), name='concert_reviews'),
    path('member-reviews/', views.MemberReviewView.as_view(), name='member_reviews'),
    # path('create-review/', views.create_review_view, name='create_review'),
    path('create-review/', views.CreateReview.as_view(), name='create_review'),
    path('about/', views.about, name='about'),
    path('<slug:slug>/', views.DetailView.as_view(), name='review_details'),
    path('<slug:slug>/edit/', views.UpdateReview.as_view(), name='update_review'),
    path('<slug:slug>/delete/', views.DeleteReview.as_view(), name='delete_review'),
    path('<int:pk>/update-comment/', views.UpdateComment.as_view(), name='update_comment'),
    path('like/<slug:slug>', views.ReviewLike.as_view(), name='like_review'),
]