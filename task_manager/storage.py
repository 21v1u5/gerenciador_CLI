from __future__ import annotations
from typing import List, Optional, Iterable
import json
from pathlib import Path
from .models import Task

DEFAULT_DB = Path(__file__).resolve().parent.parent / "tasks.json"

class TaskRepository:
    def __init__(self, db_path: Optional[Path] = None):
        self.db_path = db_path or DEFAULT_DB
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.db_path.exists():
            self._write([])


    def _read(self) -> List[Task]:
        raw = self.db_path.read_text(encoding="utf-8") if self.db_path.exists() else "[]"
        data = json.loads(raw or "[]")
        return [Task.from_dict(t) for t in data]
    

    def _write(self, tasks: Iterable[Task]) -> None:
        data = [t.to_dict() for t in tasks]
        self.db_path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

    
    def all(self) -> List[Task]:
        return self._read()


    def add(self, task: Task) -> Task:
        tasks = self._read()
        tasks.append(task)
        self._write(tasks)
        return task