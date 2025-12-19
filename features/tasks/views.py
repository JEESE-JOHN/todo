from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from features.tasks.models import Task
from features.tasks.dataclasses.request.create import CreateTaskRequest
from features.tasks.dataclasses.request.update import UpdateTaskRequest
from features.tasks.dataclasses.request.list import ListTasksRequest

from todo_project.common.common import Common
from todo_project.common.utils import Utils
from todo_project.common.constants import Constants

class TasksView:
    
    @Common().exception_handler
    def create_extract(self, params: CreateTaskRequest) -> Response:
        task = Task.create_from_dataclass(params)
        return Response(
            status=status.HTTP_201_CREATED,
            data=Utils.success_response_data(
                message="Task created successfully",
                data=task.to_response_dataclass().__dict__
            )
        )

    @Common().exception_handler
    def update_extract(self, params: UpdateTaskRequest) -> Response:
        task = get_object_or_404(Task, id=params.task_id)
        task.update_from_dataclass(params)
        
        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response_data(
                message="Task updated successfully",
                data=task.to_response_dataclass().__dict__
            )
        )

    @Common().exception_handler
    def list_extract(self, params: ListTasksRequest, token_payload=None) -> Response:
        tasks = Task.objects.all().order_by('-id')
        pages = Paginator(tasks, params.limit)
        
        if pages.num_pages < params.page_num:
             raise ValueError(Constants.page_num_exceeded)
             
        page_data = pages.page(params.page_num)
        
        data = [task.to_response_dataclass().__dict__ for task in page_data]
        
        present_url = ""
        if token_payload and hasattr(token_payload, 'present_url'):
            present_url = token_payload.present_url
        
        response_data = Utils.add_page_parameter(
            final_data=data,
            page_num=params.page_num,
            total_page=pages.num_pages,
            total_count=pages.count,
            present_url=present_url,
            next_page_required=True if pages.num_pages != params.page_num else False
        )
        
        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response_data(
                message="Tasks listed successfully",
                data=response_data
            )
        )

    @Common().exception_handler
    def get_extract(self, request) -> Response:
        task_id = request.query_params.get('task_id')
        if not task_id:
            raise ValueError("task_id is required")
            
        task = get_object_or_404(Task, id=task_id)
        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response_data(
                message="Task retrieved successfully",
                data=task.to_response_dataclass().__dict__
            )
        )

    @Common().exception_handler
    def delete_extract(self, request) -> Response:
        task_id = request.query_params.get('task_id')
        if not task_id:
            raise ValueError("task_id is required")
            
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        
        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response_data(message="Task deleted successfully")
        )
