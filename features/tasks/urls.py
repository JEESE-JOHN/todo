from django.urls import path
from features.tasks.controller import (
    create_task_endpoint, 
    update_task_endpoint,
    list_tasks_endpoint,
    get_task_endpoint,
    delete_task_endpoint
)

urlpatterns = [
    path('list/', list_tasks_endpoint, name='list-tasks'),
    path('create/', create_task_endpoint, name='create-task'),
    path('get/<int:task_id>/', get_task_endpoint, name='get-task'),
    path('update/<int:task_id>/', update_task_endpoint, name='update-task'),
    path('delete/<int:task_id>/', delete_task_endpoint, name='delete-task'),
]