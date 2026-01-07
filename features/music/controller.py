from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from features.music.serializers.request.create import CreateSongRequestSerializer
from features.music.serializers.request.update import UpdateSongRequestSerializer
from features.music.serializers.request.list import ListSongsRequestSerializer
from features.music.serializers.response.get_all import SongSingleResponseSerializer, SongGetAllResponseSerializer

from features.music.views import MusicView
from todo_project.common.utils import Utils
from todo_project.common.serializer_validations import SerializerValidations
from todo_project.common.swagger import SwaggerPage

class MusicController:
    view = MusicView()

    @extend_schema(
        description="Add a new song",
        request=CreateSongRequestSerializer,
        responses=SwaggerPage.response(response=SongSingleResponseSerializer)
    )
    @api_view(['POST'])
    @SerializerValidations(serializer=CreateSongRequestSerializer)
    def create(request: Request) -> Response:
        return MusicController.view.create(request.params)

    @extend_schema(
        description="List all songs with pagination",
        parameters=SwaggerPage.get_all_parameters(),
        responses=SwaggerPage.response(response=SongGetAllResponseSerializer)
    )
    @api_view(['GET'])
    @SerializerValidations(serializer=ListSongsRequestSerializer)
    def get_all(request: Request) -> Response:
        return MusicController.view.get_all(params=request.params, request=request)

    @extend_schema(
        description="Get a single song by ID",
        parameters=SwaggerPage.get_parameters(names=['song_id']),
        responses=SwaggerPage.response(response=SongSingleResponseSerializer)
    )
    @api_view(['GET'])
    def get(request: Request) -> Response:
        params = Utils.get_query_params(request)
        return MusicController.view.get_one(params=params)

    @extend_schema(
        description="Update an existing song",
        request=UpdateSongRequestSerializer,
        responses=SwaggerPage.response(response=SongSingleResponseSerializer)
    )
    @api_view(['PUT'])
    @SerializerValidations(serializer=UpdateSongRequestSerializer)
    def update(request: Request) -> Response: 
        return MusicController.view.update(song_id=request.params.song_id, params=request.params)

    @extend_schema(
        description="Delete a song",
        parameters=SwaggerPage.get_parameters(names=['song_id']),
        responses=SwaggerPage.response(description="Song deleted successfully")
    )
    @api_view(['DELETE'])
    def delete(request: Request) -> Response:
        params = Utils.get_query_params(request)
        song_id = params.get('song_id')
        if not song_id:
            return Response(Utils.error_response("Validation error", "song_id is required"), status=status.HTTP_400_BAD_REQUEST)
            
        return MusicController.view.delete(song_id=int(song_id))
