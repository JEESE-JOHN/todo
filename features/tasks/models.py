from django.db import models
from typing import TYPE_CHECKING

# Import the dataclasses for type hints
from features.tasks.dataclasses.request.create import CreateTaskRequest
from features.tasks.dataclasses.request.update import UpdateTaskRequest
from features.tasks.dataclasses.response.task import TaskResponse


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create_from_dataclass(cls, data: CreateTaskRequest) -> "Task":
        """
        Create a Task row from a validated dataclass.
        """
        task = cls.objects.create(
            title=data.title,
            description=getattr(data, "description", None),
            is_completed=False,
        )
        return task

    def update_from_dataclass(self, data: UpdateTaskRequest) -> "Task":
        """
        Update this Task instance using values from the dataclass.
        Only updates fields that are not None on the dataclass (partial updates).
        """
        updated = False

        if getattr(data, "title", None) is not None:
            self.title = data.title
            updated = True

        if getattr(data, "description", None) is not None:
            self.description = data.description
            updated = True

        if getattr(data, "is_completed", None) is not None:
            self.is_completed = data.is_completed
            updated = True

        if updated:
            self.save()

        return self

    def to_response_dataclass(self) -> TaskResponse:
        return TaskResponse(
            id=self.id,
            title=self.title,
            description=self.description,
            is_completed=self.is_completed,
            created_at=self.created_at,
        )

    def __str__(self):
        return self.title