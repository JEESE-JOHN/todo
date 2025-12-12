from rest_framework import serializers

class TaskResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField(allow_null=True)
    is_completed = serializers.BooleanField()
    created_at = serializers.DateTimeField()
