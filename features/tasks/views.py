from django.shortcuts import get_object_or_404
from typing import List
from features.tasks.models import Task
from features.tasks.dataclasses.request.create import CreateTaskRequest
from features.tasks.dataclasses.request.update import UpdateTaskRequest

def create_task_logic(data: CreateTaskRequest) -> Task:
    """
    Business logic for creating a task.
    """
    task = Task.create_from_dataclass(data)
    return task

def update_task_logic(task_id: int, data: UpdateTaskRequest) -> Task:
    """
    Business logic for updating a task.
    """
    task = get_object_or_404(Task, id=task_id)
    task.update_from_dataclass(data)
    return task

def list_tasks_logic() -> List[Task]:
    """
    Business logic for listing tasks.
    """
    return list(Task.objects.all())

def get_task_logic(task_id: int) -> Task:
    """
    Business logic for retrieving a single task.
    """
    return get_object_or_404(Task, id=task_id)

def delete_task_logic(task_id: int) -> None:
    """
    Business logic for deleting a task.
    """
    task = get_object_or_404(Task, id=task_id)
    task.delete()