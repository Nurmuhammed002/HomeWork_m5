from django.urls import path
from .views import (DirectorListView,DirectorDetailView,
                    MovieListView, MovieDetailView,
                    ReviewListView, ReviewDetailView)
from .views import (movie_list_with_reviews,
                    director_list_with_movies_count)

urlpatterns = [
    path('movies/reviews/', movie_list_with_reviews, name='movie-list-with-reviews'),
    path('directors/', director_list_with_movies_count, name='director-list-with-movies-count'),
    path('directors/', DirectorListView.as_view(), name='director-list'),
    path('directors/<int:id>/', DirectorDetailView.as_view(), name='director-detail'),
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/<int:id>/', MovieDetailView.as_view(), name='movie-detail'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:id>/', ReviewDetailView.as_view(), name='review-detail'),
]
