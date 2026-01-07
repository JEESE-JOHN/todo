from rest_framework import serializers
from todo_project.common.serializers.response.api_response import ApiResponseSerializer
from features.tasks.serializers.response.task import TaskResponseSerializer

class TaskSingleResponseSerializer(ApiResponseSerializer):
    data = TaskResponseSerializer()

class TaskGetAllResponseSerializer(ApiResponseSerializer):
    data = serializers.ListField(child=TaskResponseSerializer())
