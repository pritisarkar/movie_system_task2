from django.urls import path
from .views import MovieListCreateView, WatchlistAddRemoveView, WatchlistListView

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('watchlist/', WatchlistAddRemoveView.as_view(), name='watchlist-add-remove'),
    path('watchlists/', WatchlistListView.as_view(), name='watchlist-list'),
]
