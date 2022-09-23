from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('concert-reviews/', views.ConcertView.as_view(), name='concert_reviews'),
    path('about/', views.about, name='about'),

]