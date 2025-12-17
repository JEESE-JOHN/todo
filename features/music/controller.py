from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from todo_project.utils.utils import Utilities

# Import Serializers
from features.music.serializers.request.create import CreateSongRequestSerializer
from features.music.serializers.request.update import UpdateSongRequestSerializer

# Import Dataclasses
from features.music.dataclasses.request.create import CreateSongRequest
from features.music.dataclasses.request.update import UpdateSongRequest

# Import Business Logic
from features.music import views

@api_view(['POST'])
def create_song_endpoint(request):
    """
    API Endpoint to create a song.
    """
    serializer = CreateSongRequestSerializer(data=request.data)
    if serializer.is_valid():
        try:
            # Convert to Dataclass
            dataclass_data = CreateSongRequest(**serializer.validated_data)
            
            # Call Business Logic
            song = views.create_song_logic(dataclass_data)
            
            # Return Response
            return Response(
                Utilities.success_response_data(
                    message="Song created successfully", 
                    data=song.to_response_dataclass().__dict__
                ), 
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
             return Response(
                 Utilities.error_response_data(message=str(e)), 
                 status=status.HTTP_400_BAD_REQUEST
             )
    
    return Response(
        Utilities.error_response_data(message="Validation Errors", errors=serializer.errors), 
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['PUT', 'PATCH'])
def update_song_endpoint(request, song_id):
    """
    API Endpoint to update a song.
    """
    serializer = UpdateSongRequestSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        try:
            # Convert to Dataclass
            dataclass_data = UpdateSongRequest(**serializer.validated_data)
            
            # Call Business Logic
            song = views.update_song_logic(song_id=song_id, data=dataclass_data)
            
            # Return Response
            return Response(
                Utilities.success_response_data(
                    message="Song updated successfully", 
                    data=song.to_response_dataclass().__dict__
                ), 
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                 Utilities.error_response_data(message=str(e)), 
                 status=status.HTTP_400_BAD_REQUEST
             )

    return Response(
        Utilities.error_response_data(message="Validation Errors", errors=serializer.errors), 
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['GET'])
def list_songs_endpoint(request):
    """
    API Endpoint to list all songs.
    """
    songs = views.list_songs_logic()
    data = [song.to_response_dataclass().__dict__ for song in songs]
    return Response(
        Utilities.success_response_data(message="Songs listed successfully", data=data), 
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
def get_song_endpoint(request, song_id):
    """
    API Endpoint to retrieve a song.
    """
    try:
        song = views.get_song_logic(song_id)
        return Response(
            Utilities.success_response_data(
                message="Song retrieved successfully", 
                data=song.to_response_dataclass().__dict__
            ), 
            status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
             Utilities.error_response_data(message=str(e)), 
             status=status.HTTP_404_NOT_FOUND
         )

@api_view(['DELETE'])
def delete_song_endpoint(request, song_id):
    """
    API Endpoint to delete a song.
    """
    try:
        views.delete_song_logic(song_id)
        return Response(
             Utilities.success_response_data(message="Song deleted successfully"), 
             status=status.HTTP_204_NO_CONTENT
         )
    except Exception as e:
        return Response(
             Utilities.error_response_data(message=str(e)), 
             status=status.HTTP_404_NOT_FOUND
         )
