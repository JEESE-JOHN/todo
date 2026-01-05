from dataclasses import dataclass
from datetime import datetime

@dataclass
class ArtistResponse:
    id: int
    song_id: int
    artist_name: str
    song_title: str
    bio: str
    created_at: datetime
