from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from features.tasks.models import Task
from features.tasks.dataclasses.request.create import CreateTaskRequest
from features.tasks.dataclasses.request.update import UpdateTaskRequest

from todo_project.common.common import Common
from todo_project.common.utils import Utils

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

from django.core.paginator import Paginator
from features.tasks.dataclasses.request.list import ListTasksRequest
from todo_project.common.constants import Constants

class TasksView:
    
    @Common().exception_handler
    def list_extract(self, params: ListTasksRequest, token_payload=None) -> Response:
        tasks = Task.objects.all().order_by('-id') # Ordering is important for pagination
        pages = Paginator(tasks, params.limit)
        
        if pages.num_pages < params.page_num:
             # Using Value Error as caught by Common decorator
             raise ValueError(Constants.page_num_exceeded)
             
        page_data = pages.page(params.page_num)
        
        data = [task.to_response_dataclass().__dict__ for task in page_data]
        
        # We need present_url to construct next page url. 
        # In erp_backend controller passes `request.params` and `token_payload` 
        # but Utils usually expects `present_url` from somewhere.
        # Check Controller again: 
        # `BillingView().get_all_extract(params=request.params, token_payload=request.payload)`
        # Where does `present_url` come from? 
        # Ah, `token_payload.present_url` in erp_backend!
        # Since we don't have full auth/payload logic, we can construct it or pass request object.
        # But `list_extract` signature in my controller call is:
        # `TasksView().list_extract(params=request.params, token_payload=getattr(request, 'payload', None))`
        # I should probably just pass `request` object if I want to be simpler, 
        # OR mock the payload structure.
        # For this Todo app, I'll pass `present_url` via a simple hack or just use request.build_absolute_uri() inside View?
        # BUT View is supposed to be business logic agnostic of Request object ideally (though erp_backend mixes it).
        # erp_backend's `token_payload` has `present_url`.
        # I'll modify Controller to pass `present_url` in `token_payload` or separate arg.
        # Let's simple use a dict for `token_payload` in controller if it's None.
        
        present_url = ""
        if token_payload and hasattr(token_payload, 'present_url'):
            present_url = token_payload.present_url
        
        # Wait, if token_payload is None (which it is currently), we need a fallback.
        # I will modify Controller to pass request to extract URL or just pass URL.
        # Let's update `list_extract` signature to accept `request` as optional or change Controller?
        # NO, Controller calls `list_extract(params=...)`.
        # I will update Controller to pass `present_url` as specific arg or inside dummy payload.
        # Let's assume for now I'll fix Controller in next step or use empty string.
        
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