from django.contrib.auth.models import User
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlists')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'movie')  # Ensure no duplicate entries

    def __str__(self):
        return f"{self.user.username}'s watchlist - {self.movie.title}"
