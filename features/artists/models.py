from django.db import models
from features.music.models import Song

class Artist(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='artists')
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, song_id, bio):
        return cls.objects.create(
            song_id=song_id,
            bio=bio,
        )

    @classmethod
    def get_all(cls):
        return cls.objects.all().order_by('-id')

    @classmethod
    def get_one(cls, artist_id):
        try:
            return cls.objects.get(id=artist_id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def update(cls, artist_id, song_id=None, bio=None):
        artist = cls.get_one(artist_id)
        if not artist:
            return None
        
        if song_id is not None:
            artist.song_id = song_id
        if bio is not None:
            artist.bio = bio
        
        artist.save()
        return artist

    @classmethod
    def delete_one(cls, artist_id):
        artist = cls.get_one(artist_id)
        if artist:
            artist.delete()
            return True
        return False

    def __str__(self):
        return f"Artist for {self.song.title}"
