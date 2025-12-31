from django.urls import path
from features.music.controller import MusicController

urlpatterns = [
    path('create/', MusicController.create, name='music-create'),
    path('update/', MusicController.update, name='music-update'),
    path('list/', MusicController.get_all, name='music-list'),
    path('get/', MusicController.get, name='music-get'),
    path('delete/', MusicController.delete, name='music-delete'),
]
