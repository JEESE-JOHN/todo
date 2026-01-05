from django.urls import path
from features.artists.controller import ArtistController

urlpatterns = [
    path('create', ArtistController.create, name='artist-create'),
    path('list', ArtistController.get_all, name='artist-list'),
    path('get', ArtistController.get, name='artist-get'),
    path('update', ArtistController.update, name='artist-update'),
    path('delete', ArtistController.delete, name='artist-delete'),
]
