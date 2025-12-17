from django.db import models
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from features.music.dataclasses.request.create import CreateSongRequest
    from features.music.dataclasses.request.update import UpdateSongRequest
    from features.music.dataclasses.response.song import SongResponse


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create_from_dataclass(cls, data: "CreateSongRequest") -> "Song":
        """
        Create a Song row from a validated dataclass.
        """
        song = cls.objects.create(
            title=data.title,
            artist=data.artist,
        )
        return song

    def update_from_dataclass(self, data: "UpdateSongRequest") -> "Song":
        """
        Update this Song instance using values from the dataclass.
        Only updates fields that are not None on the dataclass (partial updates).
        """
        updated = False

        if getattr(data, "title", None) is not None:
            self.title = data.title
            updated = True

        if getattr(data, "artist", None) is not None:
            self.artist = data.artist
            updated = True

        if updated:
            self.save()

        return self

    def to_response_dataclass(self) -> "SongResponse":
        # Import internally to avoid circular dependency if needed, 
        # but type hinting with TYPE_CHECKING handles most cases.
        # However, at runtime, we need the class.
        from features.music.dataclasses.response.song import SongResponse
        
        return SongResponse(
            id=self.id,
            title=self.title,
            artist=self.artist,
            created_at=self.created_at,
        )

    def __str__(self):
        return f"{self.title} by {self.artist}"
