from dataclasses import dataclass
from datetime import datetime

@dataclass
class SongResponse:
    id: int
    title: str
    artist: str
    created_at: datetime
