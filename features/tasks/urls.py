from django.urls import path
from features.tasks.controller import TasksController

urlpatterns = [
    path('list/', TasksController.get_all, name='list-tasks'),
    path('create/', TasksController.create, name='create-task'),
    path('get/', TasksController.get, name='get-task'),
    path('update/', TasksController.update, name='update-task'),
    path('delete/', TasksController.delete, name='delete-task'),
]