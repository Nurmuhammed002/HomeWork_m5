from django.urls import path
from movie_app import views

urlpatterns = [
    path('directors/', views.DirectorListView.as_view(), name='director-list'),
    path('directors/<int:pk>/', views.DirectorDetailView.as_view(), name='director-detail'),
    path('directors/create/', views.DirectorCreateView.as_view(), name='director-create'),
    path('directors/<int:pk>/update/', views.DirectorUpdateDeleteView.as_view(), name='director-update-delete'),

    path('movies/', views.MovieListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('movies/create/', views.MovieCreateView.as_view(), name='movie-create'),
    path('movies/<int:pk>/update/', views.MovieUpdateDeleteView.as_view(), name='movie-update-delete'),

    path('reviews/', views.ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/create/', views.ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:pk>/update/', views.ReviewUpdateDeleteView.as_view(), name='review-update-delete'),

    path('directors/movies/count/', views.DirectorListWithMoviesCountView.as_view(), name='director-list-with-movies-count'),
    path('movies/reviews/', views.MovieListWithReviewsView.as_view(), name='movie-list-with-reviews'),
]