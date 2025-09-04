from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Literal, Dict, Any
from datetime import datetime
import uuid

Priority = Literal["baixa", "media", "alta"]
Status = Literal["fazer", "fazendo", "feito"]

def _short_id() -> str:
    return uuid.uuid4().hex[:8]


def _parse_date(s: Optional[str]) -> Optional[str]:
    if not s:
        return None
    try:
        datetime.strptime(s, "%d-%m-%Y")
        return s
    except ValueError:
        raise ValueError("formato de data invalido, tente DD-MM-YYYY")
    

@dataclass
class Task:
    title: str
    due: Optional[str] = None # DD-MM-YYYY
    priority: Priority = "media"
    status: Status = "fazer"
    tags: List[str] = field(default_factory=list)
    id: str = field(default_factory=_short_id)


    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
    

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        return cls(
            id=data.get("id") or _short_id(),
            title=data["title"],
            due=_parse_date(data.get("due")),
            priority=data.get("priority", "media"),
            status=data.get("status", "fazer"),
            tags=data.get("tags") or [],
        )
    

    def update(self, **kwargs) -> None:
        if "title" in kwargs and kwargs["title"]:
            self.title = kwargs["title"]
        if "due" in kwargs:
            self.due = _parse_date(kwargs["due"])
        if "priority" in kwargs and kwargs["priority"]:
            self.priority = kwargs["priority"]
        if "status" in kwargs and kwargs["status"]:
            self.status = kwargs["status"]
        if "tags" in kwargs and kwargs["tags"] is not None:
            self.tags = kwargs["tags"] 