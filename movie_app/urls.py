from django.urls import path
from .views import (
    DirectorListView, DirectorDetailView, DirectorCreateView, DirectorUpdateDeleteView,
    MovieListView, MovieDetailView, MovieCreateView, MovieUpdateDeleteView,
    ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateDeleteView,
    movie_list_with_reviews, director_list_with_movies_count)

urlpatterns = [
    path('directors/', DirectorListView.as_view(), name='director-list'),
    path('directors/create/', DirectorCreateView.as_view(), name='director-create'),
    path('directors/<int:pk>/', DirectorDetailView.as_view(), name='director-detail'),
    path('directors/<int:pk>/edit/', DirectorUpdateDeleteView.as_view(), name='director-update-delete'),
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/create/', MovieCreateView.as_view(), name='movie-create'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movies/<int:pk>/edit/', MovieUpdateDeleteView.as_view(), name='movie-update-delete'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/<int:pk>/edit/', ReviewUpdateDeleteView.as_view(), name='review-update-delete'),
    path('movies/reviews/', movie_list_with_reviews, name='movie-list-with-reviews'),
    path('directors/movies_count/', director_list_with_movies_count, name='director-list-with-movies-count'),
]

