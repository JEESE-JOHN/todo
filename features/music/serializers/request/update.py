from rest_framework import serializers
from features.music.dataclasses.request.update import UpdateSongRequest

class UpdateSongRequestSerializer(serializers.Serializer):
    song_id = serializers.IntegerField(required=True)
    title = serializers.CharField(max_length=200, required=False)
    artist = serializers.CharField(max_length=200, required=False)

    def create(self, validated_data):
        return UpdateSongRequest(**validated_data)
