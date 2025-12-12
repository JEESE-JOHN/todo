from dataclasses import dataclass
from typing import Optional

@dataclass
class CreateTaskRequest:
    title: str
    description: Optional[str] = None
