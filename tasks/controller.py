from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Import Serializers
from tasks.serializers.request.create import CreateTaskRequestSerializer
from tasks.serializers.request.update import UpdateTaskRequestSerializer

# Import Dataclasses
from tasks.dataclasses.request.create import CreateTaskRequest
from tasks.dataclasses.request.update import UpdateTaskRequest

# Import Business Logic
from tasks import views

@api_view(['POST'])
def create_task_endpoint(request):
    """
    API Endpoint to create a task.
    """
    serializer = CreateTaskRequestSerializer(data=request.data)
    if serializer.is_valid():
        try:
            # Convert to Dataclass
            dataclass_data = CreateTaskRequest(**serializer.validated_data)
            
            # Call Business Logic
            task = views.create_task_logic(dataclass_data)
            
            # Return Response
            return Response(task.to_response_dataclass().__dict__, status=status.HTTP_201_CREATED)
        except Exception as e:
             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def update_task_endpoint(request, task_id):
    """
    API Endpoint to update a task.
    """
    serializer = UpdateTaskRequestSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        try:
            # Convert to Dataclass
            dataclass_data = UpdateTaskRequest(**serializer.validated_data)
            
            # Call Business Logic
            task = views.update_task_logic(task_id=task_id, data=dataclass_data)
            
            # Return Response
            return Response(task.to_response_dataclass().__dict__, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_tasks_endpoint(request):
    """
    API Endpoint to list all tasks.
    """
    tasks = views.list_tasks_logic()
    return Response([task.to_response_dataclass().__dict__ for task in tasks], status=status.HTTP_200_OK)

@api_view(['GET'])
def get_task_endpoint(request, task_id):
    """
    API Endpoint to retrieve a task.
    """
    try:
        task = views.get_task_logic(task_id)
        return Response(task.to_response_dataclass().__dict__, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_task_endpoint(request, task_id):
    """
    API Endpoint to delete a task.
    """
    try:
        views.delete_task_logic(task_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
