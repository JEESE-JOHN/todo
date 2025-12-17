from django.urls import path
from features.music.controller import (
    create_song_endpoint, 
    update_song_endpoint,
    list_songs_endpoint,
    get_song_endpoint,
    delete_song_endpoint
)

urlpatterns = [
    path('list/', list_songs_endpoint, name='list-songs'),
    path('create/', create_song_endpoint, name='create-song'),
    path('get/<int:song_id>/', get_song_endpoint, name='get-song'),
    path('update/<int:song_id>/', update_song_endpoint, name='update-song'),
    path('delete/<int:song_id>/', delete_song_endpoint, name='delete-song'),
]
