"""Import relevant modules for the application"""

from django.urls import path
from . import views

urlpatterns = [
     path('', views.HomeView.as_view(), name='home'),
     path('concert-reviews/', views.ConcertView.as_view(),
          name='concert_reviews'),
     path('album-reviews/', views.AlbumView.as_view(),
          name='album_reviews'),
     path('member-reviews/', views.MemberReviewView.as_view(),
          name='member_reviews'),
     path('create-review/', views.CreateReview.as_view(),
          name='create_review'),
     path('review/submit-success/', views.review_submitted,
          name='review_submit_success'),
     path('review/update-success/', views.review_updated,
          name='review_update_success'),
     path('review/delete-success/', views.review_deleted,
          name='review_delete_success'),
     path('comment/delete-success/', views.comment_deleted,
          name='comment_delete_success/'),
     path('about/', views.about, name='about'),
     path('admin-area/', views.AdminArea.as_view(), name='admin_area'),
     path('<slug:slug>/', views.DetailView.as_view(),
          name='review_details'),
     path('<slug:slug>/edit/', views.UpdateReview.as_view(),
          name='update_review'),
     path('<int:pk>/delete/', views.DeleteComment.as_view(),
          name='delete_comment'),
     path('<slug:slug>/delete/', views.DeleteReview.as_view(),
          name='delete_review'),
     path('<int:pk>/update-comment/', views.UpdateComment.as_view(),
          name='update_comment'),
     path('like/<slug:slug>', views.ReviewLike.as_view(),
          name='like_review'),
]
