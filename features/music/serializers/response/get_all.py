from rest_framework import serializers
from todo_project.common.serializers.response.api_response import ApiResponseSerializer
from features.music.serializers.response.song import SongResponseSerializer

class SongSingleResponseSerializer(ApiResponseSerializer):
    data = SongResponseSerializer()

class SongGetAllResponseSerializer(ApiResponseSerializer):
    data = serializers.ListField(child=SongResponseSerializer())
