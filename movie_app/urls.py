from django.urls import path
from .views import (DirectorListView, DirectorDetailView,
                    DirectorCreateView, DirectorUpdateDeleteView,
                    MovieListView, MovieDetailView,
                    MovieCreateView, MovieUpdateDeleteView,
                    ReviewListView, ReviewDetailView,
                    ReviewCreateView, ReviewUpdateDeleteView,
                    movie_list_with_reviews,
                    director_list_with_movies_count)

urlpatterns = [
    path('directors/', DirectorListView.as_view(), name='director-list'),
    path('directors/<int:pk>/', DirectorDetailView.as_view(), name='director-detail'),
    path('directors/create/', DirectorCreateView.as_view(), name='director-create'),
    path('directors/<int:pk>/update/', DirectorUpdateDeleteView.as_view(), name='director-update-delete'),

    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movies/create/', MovieCreateView.as_view(), name='movie-create'),
    path('movies/<int:pk>/update/', MovieUpdateDeleteView.as_view(), name='movie-update-delete'),

    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:pk>/update/', ReviewUpdateDeleteView.as_view(), name='review-update-delete'),

    path('directors/movies/count/', director_list_with_movies_count, name='director-list-with-movies-count'),
    path('movies/reviews/', movie_list_with_reviews, name='movie-list-with-reviews'),
]
