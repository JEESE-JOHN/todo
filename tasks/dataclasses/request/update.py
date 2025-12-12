from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateTaskRequest:
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None
