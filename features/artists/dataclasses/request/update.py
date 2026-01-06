from dataclasses import dataclass

@dataclass
class UpdateArtistRequest:
    artist_id: int
    song_id: int = None
    bio: str = None
