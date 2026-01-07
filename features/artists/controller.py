from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from features.artists.serializers.request.create import CreateArtistRequestSerializer
from features.artists.serializers.request.update import UpdateArtistRequestSerializer
from features.artists.serializers.request.list import ListArtistsRequestSerializer
from features.artists.serializers.response.get_all import ArtistSingleResponseSerializer, ArtistGetAllResponseSerializer

from features.artists.views import ArtistView
from todo_project.common.utils import Utils
from todo_project.common.serializer_validations import SerializerValidations
from todo_project.common.swagger import SwaggerPage

class ArtistController:
    view = ArtistView()

    @extend_schema(
        description="Create a new artist",
        request=CreateArtistRequestSerializer,
        responses=SwaggerPage.response(response=ArtistSingleResponseSerializer)
    )
    @api_view(['POST'])
    @SerializerValidations(serializer=CreateArtistRequestSerializer)
    def create(request: Request) -> Response:
        return ArtistController.view.create(request.params)

    @extend_schema(
        description="List all artists with pagination",
        parameters=SwaggerPage.get_all_parameters(),
        responses=SwaggerPage.response(response=ArtistGetAllResponseSerializer)
    )
    @api_view(['GET'])
    @SerializerValidations(serializer=ListArtistsRequestSerializer)
    def get_all(request: Request) -> Response:
        return ArtistController.view.get_all(params=request.params, request=request)

    @extend_schema(
        description="Get a single artist by ID",
        parameters=SwaggerPage.get_parameters(names=['artist_id']),
        responses=SwaggerPage.response(response=ArtistSingleResponseSerializer)
    )
    @api_view(['GET'])
    def get(request: Request) -> Response:
        params = Utils.get_query_params(request)
        return ArtistController.view.get_one(params=params)

    @extend_schema(
        description="Update an existing artist",
        request=UpdateArtistRequestSerializer,
        responses=SwaggerPage.response(response=ArtistSingleResponseSerializer)
    )
    @api_view(['PUT'])
    @SerializerValidations(serializer=UpdateArtistRequestSerializer)
    def update(request: Request) -> Response: 
        return ArtistController.view.update(artist_id=request.params.artist_id, params=request.params)

    @extend_schema(
        description="Delete an artist",
        parameters=SwaggerPage.get_parameters(names=['artist_id']),
        responses=SwaggerPage.response(description="Artist deleted successfully")
    )
    @api_view(['DELETE'])
    def delete(request: Request) -> Response:
        params = Utils.get_query_params(request)
        artist_id = params.get('artist_id')
        if not artist_id:
            return Response(Utils.error_response("Validation error", "artist_id is required"), status=status.HTTP_400_BAD_REQUEST)
            
        return ArtistController.view.delete(artist_id=int(artist_id))
