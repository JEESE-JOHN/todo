from django.shortcuts import get_object_or_404
from typing import List
from features.music.models import Song
from features.music.dataclasses.request.create import CreateSongRequest
from features.music.dataclasses.request.update import UpdateSongRequest

def create_song_logic(data: CreateSongRequest) -> Song:
    """
    Business logic for creating a song.
    """
    song = Song.create_from_dataclass(data)
    return song

def update_song_logic(song_id: int, data: UpdateSongRequest) -> Song:
    """
    Business logic for updating a song.
    """
    song = get_object_or_404(Song, id=song_id)
    song.update_from_dataclass(data)
    return song

def list_songs_logic() -> List[Song]:
    """
    Business logic for listing songs.
    """
    return list(Song.objects.all())

def get_song_logic(song_id: int) -> Song:
    """
    Business logic for retrieving a single song.
    """
    return get_object_or_404(Song, id=song_id)

def delete_song_logic(song_id: int) -> None:
    """
    Business logic for deleting a song.
    """
    song = get_object_or_404(Song, id=song_id)
    song.delete()
