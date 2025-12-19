from django.urls import path
from features.tasks.controller import TasksViewController

urlpatterns = [
    path('list/', TasksViewController.list, name='list-tasks'),
    path('create/', TasksViewController.create, name='create-task'),
    path('get/', TasksViewController.get, name='get-task'),
    path('update/', TasksViewController.update, name='update-task'),
    path('delete/', TasksViewController.delete, name='delete-task'),
]