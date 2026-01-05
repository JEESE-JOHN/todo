from dataclasses import dataclass

@dataclass
class UpdateArtistRequest:
    song_id: int = None
    bio: str = None
