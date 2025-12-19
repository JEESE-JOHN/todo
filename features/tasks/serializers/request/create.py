from rest_framework import serializers
from features.tasks.dataclasses.request.create import CreateTaskRequest

class CreateTaskRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return CreateTaskRequest(**validated_data)
