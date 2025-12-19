from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateSongRequest:
    song_id: int
    title: Optional[str] = None
    artist: Optional[str] = None
