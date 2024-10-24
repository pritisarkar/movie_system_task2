from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Movie, Watchlist
from .serializers import MovieSerializer, WatchlistSerializer

# Create and List Movies
class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

# Add or Remove Movies from Watchlist
class WatchlistAddRemoveView(generics.GenericAPIView):
    serializer_class = WatchlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        movie_id = request.data.get('movie_id')
        movie = Movie.objects.get(id=movie_id)
        watchlist, created = Watchlist.objects.get_or_create(user=request.user, movie=movie)

        if created:
            return Response({'detail': 'Movie added to watchlist.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'detail': 'Movie already in watchlist.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        movie_id = request.data.get('movie_id')
        try:
            movie = Movie.objects.get(id=movie_id)
            watchlist = Watchlist.objects.get(user=request.user, movie=movie)
            watchlist.delete()
            return Response({'detail': 'Movie removed from watchlist.'}, status=status.HTTP_204_NO_CONTENT)
        except Watchlist.DoesNotExist:
            return Response({'detail': 'Movie not found in watchlist.'}, status=status.HTTP_404_NOT_FOUND)

# List All Watchlists
class WatchlistListView(generics.ListAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    permission_classes = [permissions.IsAuthenticated]
