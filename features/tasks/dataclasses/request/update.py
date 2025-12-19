from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateTaskRequest:
    task_id: int
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None
