from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from features.artists.serializers.request.create import CreateArtistRequestSerializer
from features.artists.serializers.request.update import UpdateArtistRequestSerializer
from features.artists.serializers.request.list import ListArtistsRequestSerializer
from features.artists.views import ArtistView
from todo_project.common.utils import Utils
from todo_project.common.serializer_validations import SerializerValidations

class ArtistController:
    view = ArtistView()

    @api_view(['POST'])
    @SerializerValidations(serializer=CreateArtistRequestSerializer)
    def create(request: Request) -> Response:
        return ArtistController.view.create(request.params)

    @api_view(['GET'])
    @SerializerValidations(serializer=ListArtistsRequestSerializer)
    def get_all(request: Request) -> Response:
        return ArtistController.view.get_all(params=request.params, request=request)

    @api_view(['GET'])
    def get(request: Request) -> Response:
        params = Utils.get_query_params(request)
        return ArtistController.view.get_one(params=params)

    @api_view(['PUT'])
    @SerializerValidations(serializer=UpdateArtistRequestSerializer)
    def update(request: Request) -> Response: 
        return ArtistController.view.update(artist_id=request.params.artist_id, params=request.params)

    @api_view(['DELETE'])
    def delete(request: Request) -> Response:
        params = Utils.get_query_params(request)
        artist_id = params.get('artist_id')
        if not artist_id:
            return Response(Utils.error_response("Validation error", "artist_id is required"), status=status.HTTP_400_BAD_REQUEST)
            
        return ArtistController.view.delete(artist_id=int(artist_id))
