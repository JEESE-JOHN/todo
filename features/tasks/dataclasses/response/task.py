from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class TaskResponse:
    id: int
    title: str
    is_completed: bool
    created_at: datetime
    description: Optional[str] = None
