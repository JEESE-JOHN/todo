from dataclasses import dataclass
from typing import Optional

@dataclass
class ListTasksRequest:
    page_num: int = 1
    limit: int = 10
    user_id: Optional[str] = None # Following standard pattern, logic might use this filter if needed
