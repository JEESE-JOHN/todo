from rest_framework import serializers

class UpdateSongRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200, required=False)
    artist = serializers.CharField(max_length=200, required=False)
