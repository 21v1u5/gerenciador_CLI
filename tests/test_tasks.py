from task_manager.storage import TaskRepository
from task_manager.models import Task

def setup_function():
    import os
    from task_manager.storage import DEFAULT_DB
    if DEFAULT_DB.exists():
        os.remove(DEFAULT_DB)


def test_add_and_list():
    repo = TaskRepository()
    t = Task(title="Estudar python", priority="alta", tags=["estudo","python"])
    repo.add(t)
    tasks = repo.all()
    assert len(tasks) == 1
    assert tasks[0].title == "Estudar python"
    assert tasks[0].priority == "alta"
    assert "python" in tasks[0].tags