from rest_framework import status
from rest_framework.response import Response
from django.core.paginator import Paginator

from features.tasks.models import Task
from features.tasks.serializers.response.task import TaskResponseSerializer
from features.tasks.dataclasses.request.create import CreateTaskRequest
from features.tasks.dataclasses.request.update import UpdateTaskRequest

from todo_project.common.common import Common
from todo_project.common.utils import Utils
from todo_project.common.constants import Constants

class TasksView:
    def create(self, params):
        task = Task.create(
            title=params.title,
            description=params.description,
            is_completed=False
        )
        data = TaskResponseSerializer(task).data
        return Response(Utils.success_response("Task created successfully", data), status=status.HTTP_201_CREATED)

    def get_all(self, params, request):
        page_num = int(params.page_num)
        limit = int(params.limit)

        qs = Task.get_all()

        pages = Paginator(qs, limit)

        if pages.num_pages < page_num:
            return Response(
                status=status.HTTP_200_OK,
                data=Utils.error_response("Invalid page", "Page number exceeded")
            )

        page = pages.page(page_num)

        data = TaskResponseSerializer(page.object_list, many=True).data

        print(f"DEBUG: request type: {type(request)}")
        try:
            full_path = request.get_full_path()
            print(f"DEBUG: full_path: {full_path}")
        except Exception as e:
            print(f"DEBUG: get_full_path failed: {e}")
            full_path = ""

        data = Utils.add_page_parameter(
            final_data=data,
            page_num=page_num,
            total_page=pages.num_pages,
            total_count=pages.count,
            present_url=full_path,
            next_page_required=pages.num_pages != page_num
        )

        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response("Data fetched successfully", data)
        )

    def get_one(self, params: dict):
        task_id = params.get("task_id")

        if not task_id:
            return Response(
                Utils.error_response("Validation error", "task_id is required"), status=status.HTTP_400_BAD_REQUEST)

        task = Task.get_one(int(task_id))
        if not task:
            return Response(
                Utils.error_response("Task not found", f"id {task_id} does not exist"), status=status.HTTP_200_OK)

        data = TaskResponseSerializer(task).data
        return Response(Utils.success_response("Data fetched successfully", data), status=status.HTTP_200_OK)

    def update(self, task_id, params):
        task = Task.update(
            task_id,
            title=params.title,
            description=params.description,
            is_completed=params.is_completed
        )
        if not task:
            return Response(Utils.error_response("Task not found", f"id {task_id} does not exist"), status=status.HTTP_200_OK)
        data = TaskResponseSerializer(task).data
        return Response(Utils.success_response("Task updated successfully", data), status=status.HTTP_200_OK)

    def delete(self, task_id: int):
        success = Task.delete_one(task_id)
        if not success:
            return Response(Utils.error_response("Task not found", f"id {task_id} does not exist"), status=status.HTTP_200_OK)
        return Response(Utils.success_response("Task deleted successfully"), status=status.HTTP_200_OK)
