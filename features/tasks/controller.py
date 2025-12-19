from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from features.tasks.serializers.request.create import CreateTaskRequestSerializer
from features.tasks.serializers.request.update import UpdateTaskRequestSerializer

from features.tasks.views import TasksView
from todo_project.common.serializer_validations import SerializerValidations

from features.tasks.serializers.request.list import ListTasksRequestSerializer

class TasksViewController:

    @api_view(['POST'])
    @SerializerValidations(serializer=CreateTaskRequestSerializer, 
                           exec_func='TasksView().create_extract(request)').validate
    def create(request: Request) -> Response:
        return TasksView().create_extract(params=request.params)

    @api_view(['PUT', 'PATCH'])
    @SerializerValidations(serializer=UpdateTaskRequestSerializer,
                           exec_func='TasksView().update_extract(request)').validate
    def update(request: Request) -> Response: 
        return TasksView().update_extract(params=request.params)

    @api_view(['GET'])
    @SerializerValidations(serializer=ListTasksRequestSerializer,
                           exec_func='TasksView().list_extract(request)').validate
    def list(request: Request) -> Response:
        # Mocking payload with present_url for pagination
        payload = type('Payload', (), {'present_url': request.build_absolute_uri()})()
        return TasksView().list_extract(params=request.params, token_payload=payload)

    @api_view(['GET'])
    def get(request: Request) -> Response:
        return TasksView().get_extract(request)

    @api_view(['DELETE'])
    def delete(request: Request) -> Response:
        return TasksView().delete_extract(request)
