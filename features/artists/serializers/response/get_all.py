from rest_framework import serializers
from todo_project.common.serializers.response.api_response import ApiResponseSerializer
from features.artists.serializers.response.artist import ArtistResponseSerializer

class ArtistSingleResponseSerializer(ApiResponseSerializer):
    data = ArtistResponseSerializer()

class ArtistGetAllResponseSerializer(ApiResponseSerializer):
    data = serializers.ListField(child=ArtistResponseSerializer())
