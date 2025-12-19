from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from features.music.serializers.request.create import CreateSongRequestSerializer
from features.music.serializers.request.update import UpdateSongRequestSerializer
from features.music.serializers.request.list import ListSongsRequestSerializer

from features.music.views import MusicView
from todo_project.common.serializer_validations import SerializerValidations

class MusicViewController:

    @api_view(['POST'])
    @SerializerValidations(serializer=CreateSongRequestSerializer, 
                           exec_func='MusicView().create_extract(request)').validate
    def create(request: Request) -> Response:
        return MusicView().create_extract(params=request.params)

    @api_view(['PUT', 'PATCH'])
    @SerializerValidations(serializer=UpdateSongRequestSerializer,
                           exec_func='MusicView().update_extract(request)').validate
    def update(request: Request) -> Response: 
        return MusicView().update_extract(params=request.params)

    @api_view(['GET'])
    @SerializerValidations(serializer=ListSongsRequestSerializer,
                           exec_func='MusicView().list_extract(request)').validate
    def list(request: Request) -> Response:
        payload = type('Payload', (), {'present_url': request.build_absolute_uri()})()
        return MusicView().list_extract(params=request.params, token_payload=payload)

    @api_view(['GET'])
    def get(request: Request) -> Response:
        return MusicView().get_extract(request)

    @api_view(['DELETE'])
    def delete(request: Request) -> Response:
        return MusicView().delete_extract(request)
