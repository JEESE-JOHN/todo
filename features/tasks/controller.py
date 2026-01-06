from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from features.tasks.serializers.request.create import CreateTaskRequestSerializer
from features.tasks.serializers.request.update import UpdateTaskRequestSerializer
from features.tasks.serializers.request.list import ListTasksRequestSerializer

from features.tasks.views import TasksView
from todo_project.common.utils import Utils
from todo_project.common.serializer_validations import SerializerValidations

class TasksController:
    view = TasksView()

    @api_view(['POST'])
    @SerializerValidations(serializer=CreateTaskRequestSerializer)
    def create(request: Request) -> Response:
        return TasksController.view.create(request.params)

    @api_view(['GET'])
    @SerializerValidations(serializer=ListTasksRequestSerializer)
    def get_all(request: Request) -> Response:
        return TasksController.view.get_all(params=request.params, request=request)

    @api_view(['GET'])
    def get(request: Request) -> Response:
        params = Utils.get_query_params(request)
        return TasksController.view.get_one(params=params)

    @api_view(['PUT'])
    @SerializerValidations(serializer=UpdateTaskRequestSerializer)
    def update(request: Request) -> Response: 
        return TasksController.view.update(task_id=request.params.task_id, params=request.params)

    @api_view(['DELETE'])
    def delete(request: Request) -> Response:
        params = Utils.get_query_params(request)
        task_id = params.get('task_id')
        if not task_id:
            return Response(Utils.error_response("Validation error", "task_id is required"), status=status.HTTP_400_BAD_REQUEST)
            
        return TasksController.view.delete(task_id=int(task_id))
