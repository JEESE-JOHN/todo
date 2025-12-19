from rest_framework import serializers
from features.tasks.dataclasses.request.update import UpdateTaskRequest

class UpdateTaskRequestSerializer(serializers.Serializer):
    task_id = serializers.IntegerField()
    title = serializers.CharField(max_length=200, required=False)
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    is_completed = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return UpdateTaskRequest(**validated_data)
