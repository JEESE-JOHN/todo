from rest_framework import serializers
from features.music.dataclasses.request.list import ListSongsRequest

class ListSongsRequestSerializer(serializers.Serializer):
    page_num = serializers.IntegerField(required=False, default=1)
    limit = serializers.IntegerField(required=False, default=10)
    artist = serializers.CharField(required=False, allow_null=True)

    def create(self, validated_data):
        return ListSongsRequest(**validated_data)
