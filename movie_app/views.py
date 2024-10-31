from rest_framework import generics
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer

class DirectorListView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorDetailView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorCreateView(generics.CreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieCreateView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class DirectorListWithMoviesCountView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        directors = Director.objects.all()
        director_data = []

        for director in directors:
            director_data.append({
                'name': director.name,
                'movies_count': director.movies.count(),
            })

        return Response(director_data)

class MovieListWithReviewsView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        movie_data = []

        for movie in movies:
            reviews = movie.reviews.all()
            total_stars = sum([review.stars for review in reviews])
            avg_rating = total_stars / reviews.count() if reviews.count() > 0 else 0
            movie_data.append({
                'title': movie.title,
                'reviews': [review.text for review in reviews],
                'average_rating': avg_rating,
            })

        return Response(movie_data)
