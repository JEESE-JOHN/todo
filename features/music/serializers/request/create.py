from rest_framework import serializers

class CreateSongRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    artist = serializers.CharField(max_length=200)
