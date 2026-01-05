from rest_framework import serializers
from features.artists.dataclasses.request.create import CreateArtistRequest

class CreateArtistRequestSerializer(serializers.Serializer):
    song_id = serializers.IntegerField()
    bio = serializers.CharField()

    def create(self, validated_data):
        return CreateArtistRequest(**validated_data)
