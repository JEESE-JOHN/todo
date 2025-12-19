from dataclasses import dataclass
from typing import Optional

@dataclass
class ListSongsRequest:
    page_num: int = 1
    limit: int = 10
    artist: Optional[str] = None
