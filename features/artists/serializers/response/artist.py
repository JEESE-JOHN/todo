from rest_framework import serializers

class ArtistResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    song_id = serializers.IntegerField()
    artist_name = serializers.CharField(source='song.artist')
    song_title = serializers.CharField(source='song.title')
    bio = serializers.CharField()
    created_at = serializers.DateTimeField()
