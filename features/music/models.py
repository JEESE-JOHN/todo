from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, title, artist):
        return cls.objects.create(
            title=title,
            artist=artist,
        )

    @classmethod
    def get_all(cls):
        return cls.objects.all().order_by('-id')

    @classmethod
    def get_one(cls, song_id):
        try:
            return cls.objects.get(id=song_id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def update(cls, song_id, title=None, artist=None):
        song = cls.get_one(song_id)
        if not song:
            return None
        
        if title is not None:
            song.title = title
        if artist is not None:
            song.artist = artist
        
        song.save()
        return song

    @classmethod
    def delete_one(cls, song_id):
        song = cls.get_one(song_id)
        if song:
            song.delete()
            return True
        return False

    def to_response_dataclass(self):
        from features.music.dataclasses.response.song import SongResponse
        
        return SongResponse(
            id=self.id,
            title=self.title,
            artist=self.artist,
            created_at=self.created_at,
        )

    def __str__(self):
        return f"{self.title} by {self.artist}"
