from rest_framework import serializers
from features.music.dataclasses.request.create import CreateSongRequest

class CreateSongRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    artist = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return CreateSongRequest(**validated_data)
