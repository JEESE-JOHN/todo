from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from features.music.serializers.request.create import CreateSongRequestSerializer
from features.music.serializers.request.update import UpdateSongRequestSerializer

from features.music.views import MusicView
from todo_project.common.utils import Utils

class MusicController:
    view = MusicView()

    @api_view(['POST'])
    def create(request: Request) -> Response:
        serializer = CreateSongRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = serializer.save()
        return MusicController.view.create(params)

    @api_view(['GET'])
    def get_all(request: Request) -> Response:
        return MusicController.view.get_all(request=request)

    @api_view(['GET'])
    def get(request: Request) -> Response:
        params = Utils.get_query_params(request)
        return MusicController.view.get_one(params=params)

    @api_view(['PUT'])
    def update(request: Request) -> Response: 
        params_qs = Utils.get_query_params(request)
        song_id = params_qs.get('song_id')
        if not song_id:
            return Response(Utils.error_response("Validation error", "song_id is required"), status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UpdateSongRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = serializer.save()
        return MusicController.view.update(song_id=int(song_id), params=params)

    @api_view(['DELETE'])
    def delete(request: Request) -> Response:
        params = Utils.get_query_params(request)
        song_id = params.get('song_id')
        if not song_id:
            return Response(Utils.error_response("Validation error", "song_id is required"), status=status.HTTP_400_BAD_REQUEST)
            
        return MusicController.view.delete(song_id=int(song_id))
