from dataclasses import dataclass

@dataclass
class CreateArtistRequest:
    song_id: int
    bio: str
