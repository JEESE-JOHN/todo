from rest_framework import serializers

class FailureResponseSerializer(serializers.Serializer):
    status = serializers.BooleanField(default=False)
    message = serializers.CharField()
    error = serializers.ListField(child=serializers.CharField(), required=False)
