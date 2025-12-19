from django.urls import path
from features.music.controller import MusicViewController

urlpatterns = [
    path('create/', MusicViewController.create, name='music-create'),
    path('update/', MusicViewController.update, name='music-update'),
    path('list/', MusicViewController.list, name='music-list'),
    path('get/', MusicViewController.get, name='music-get'),
    path('delete/', MusicViewController.delete, name='music-delete'),
]
