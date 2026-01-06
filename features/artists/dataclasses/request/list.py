from dataclasses import dataclass
from typing import Optional

@dataclass
class ListArtistsRequest:
    page_num: int = 1
    limit: int = 10
    song_id: Optional[int] = None
