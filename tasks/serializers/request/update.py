from rest_framework import serializers

class UpdateTaskRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200, required=False)
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    is_completed = serializers.BooleanField(required=False)
