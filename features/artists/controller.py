from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from features.artists.serializers.request.create import CreateArtistRequestSerializer
from features.artists.serializers.request.update import UpdateArtistRequestSerializer
from features.artists.views import ArtistView
from todo_project.common.utils import Utils

class ArtistController:
    view = ArtistView()

    @api_view(['POST'])
    def create(request: Request) -> Response:
        serializer = CreateArtistRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = serializer.save()
        return ArtistController.view.create(params)

    @api_view(['GET'])
    def get_all(request: Request) -> Response:
        return ArtistController.view.get_all(request=request)

    @api_view(['GET'])
    def get(request: Request) -> Response:
        params = Utils.get_query_params(request)
        return ArtistController.view.get_one(params=params)

    @api_view(['PUT'])
    def update(request: Request) -> Response: 
        params_qs = Utils.get_query_params(request)
        artist_id = params_qs.get('artist_id')
        if not artist_id:
            return Response(Utils.error_response("Validation error", "artist_id is required"), status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UpdateArtistRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = serializer.save()
        return ArtistController.view.update(artist_id=int(artist_id), params=params)

    @api_view(['DELETE'])
    def delete(request: Request) -> Response:
        params = Utils.get_query_params(request)
        artist_id = params.get('artist_id')
        if not artist_id:
            return Response(Utils.error_response("Validation error", "artist_id is required"), status=status.HTTP_400_BAD_REQUEST)
            
        return ArtistController.view.delete(artist_id=int(artist_id))
