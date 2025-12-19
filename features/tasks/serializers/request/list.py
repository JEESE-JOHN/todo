from rest_framework import serializers
from features.tasks.dataclasses.request.list import ListTasksRequest

class ListTasksRequestSerializer(serializers.Serializer):
    page_num = serializers.IntegerField(required=False, default=1)
    limit = serializers.IntegerField(required=False, default=10)
    user_id = serializers.CharField(required=False, allow_null=True)

    def create(self, validated_data):
        return ListTasksRequest(**validated_data)
