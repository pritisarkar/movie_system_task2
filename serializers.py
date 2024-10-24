from rest_framework import serializers
from .models import Movie, Watchlist

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description']

class WatchlistSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)  # Nested Movie details

    class Meta:
        model = Watchlist
        fields = ['id', 'user', 'movie']
        read_only_fields = ['user']  # User is set automatically
