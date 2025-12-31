from rest_framework import serializers

class SongResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    artist = serializers.CharField()
    created_at = serializers.DateTimeField()
