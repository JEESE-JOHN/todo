from dataclasses import dataclass

@dataclass
class CreateSongRequest:
    title: str
    artist: str
