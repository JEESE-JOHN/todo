from rest_framework import serializers
from features.artists.dataclasses.request.update import UpdateArtistRequest

class UpdateArtistRequestSerializer(serializers.Serializer):
    artist_id = serializers.IntegerField(required=True)
    song_id = serializers.IntegerField(required=False)
    bio = serializers.CharField(required=False)

    def create(self, validated_data):
        return UpdateArtistRequest(**validated_data)
