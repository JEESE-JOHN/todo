from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateSongRequest:
    title: Optional[str] = None
    artist: Optional[str] = None
