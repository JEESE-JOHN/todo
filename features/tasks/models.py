from django.db import models
from features.tasks.dataclasses.response.task import TaskResponse


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, title, description=None, is_completed=False):
        return cls.objects.create(
            title=title,
            description=description,
            is_completed=is_completed
        )

    @classmethod
    def get_all(cls):
        return cls.objects.all().order_by('-id')

    @classmethod
    def get_one(cls, task_id):
        try:
            return cls.objects.get(id=task_id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def update(cls, task_id, title=None, description=None, is_completed=None):
        task = cls.get_one(task_id)
        if not task:
            return None
        
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if is_completed is not None:
            task.is_completed = is_completed
        
        task.save()
        return task

    @classmethod
    def delete_one(cls, task_id):
        task = cls.get_one(task_id)
        if task:
            task.delete()
            return True
        return False

    def to_response_dataclass(self):
        return TaskResponse(
            id=self.id,
            title=self.title,
            description=self.description,
            is_completed=self.is_completed,
            created_at=self.created_at,
        )

    def __str__(self):
        return self.title