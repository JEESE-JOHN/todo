from rest_framework import serializers
from features.artists.dataclasses.request.list import ListArtistsRequest

class ListArtistsRequestSerializer(serializers.Serializer):
    page_num = serializers.IntegerField(required=False, default=1)
    limit = serializers.IntegerField(required=False, default=10)
    song_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return ListArtistsRequest(**validated_data)
