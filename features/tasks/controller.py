from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from features.tasks.serializers.request.create import CreateTaskRequestSerializer
from features.tasks.serializers.request.update import UpdateTaskRequestSerializer

from features.tasks.views import TasksView
from todo_project.common.utils import Utils

class TasksController:
    view = TasksView()

    @api_view(['POST'])
    def create(request: Request) -> Response:
        serializer = CreateTaskRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = serializer.save()
        return TasksController.view.create(params)

    @api_view(['GET'])
    def get_all(request: Request) -> Response:
        return TasksController.view.get_all(request=request)

    @api_view(['GET'])
    def get(request: Request) -> Response:
        params = Utils.get_query_params(request)
        return TasksController.view.get_one(params=params)

    @api_view(['PUT'])
    def update(request: Request) -> Response: 
        params_qs = Utils.get_query_params(request)
        task_id = params_qs.get('task_id')
        if not task_id:
            return Response(Utils.error_response("Validation error", "task_id is required"), status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UpdateTaskRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = serializer.save()
        return TasksController.view.update(task_id=int(task_id), params=params)

    @api_view(['DELETE'])
    def delete(request: Request) -> Response:
        params = Utils.get_query_params(request)
        task_id = params.get('task_id')
        if not task_id:
            return Response(Utils.error_response("Validation error", "task_id is required"), status=status.HTTP_400_BAD_REQUEST)
            
        return TasksController.view.delete(task_id=int(task_id))
