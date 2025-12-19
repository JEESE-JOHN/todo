from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from typing import List

from features.music.models import Song
from features.music.dataclasses.request.create import CreateSongRequest
from features.music.dataclasses.request.update import UpdateSongRequest
from features.music.dataclasses.request.list import ListSongsRequest

from todo_project.common.common import Common
from todo_project.common.utils import Utils
from todo_project.common.constants import Constants

class MusicView:
    
    @Common().exception_handler
    def create_extract(self, params: CreateSongRequest) -> Response:
        song = Song.create_from_dataclass(params)
        return Response(
            status=status.HTTP_201_CREATED,
            data=Utils.success_response_data(
                message="Song created successfully",
                data=song.to_response_dataclass().__dict__
            )
        )

    @Common().exception_handler
    def update_extract(self, params: UpdateSongRequest) -> Response:
        song = get_object_or_404(Song, id=params.song_id)
        song.update_from_dataclass(params)
        
        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response_data(
                message="Song updated successfully",
                data=song.to_response_dataclass().__dict__
            )
        )

    @Common().exception_handler
    def list_extract(self, params: ListSongsRequest, token_payload=None) -> Response:
        songs = Song.objects.all().order_by('-id')
        if params.artist:
            songs = songs.filter(artist__icontains=params.artist)
            
        pages = Paginator(songs, params.limit)
        
        if pages.num_pages < params.page_num and params.page_num > 1:
             raise ValueError(Constants.page_num_exceeded)
             
        page_data = pages.page(params.page_num)
        data = [song.to_response_dataclass().__dict__ for song in page_data]
        
        present_url = ""
        if token_payload and hasattr(token_payload, 'present_url'):
            present_url = token_payload.present_url
        
        response_data = Utils.add_page_parameter(
            final_data=data,
            page_num=params.page_num,
            total_page=pages.num_pages,
            total_count=pages.count,
            present_url=present_url,
            next_page_required=True if pages.num_pages != params.page_num else False
        )
        
        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response_data(
                message="Songs listed successfully",
                data=response_data
            )
        )

    @Common().exception_handler
    def get_extract(self, request) -> Response:
        song_id = request.query_params.get('song_id')
        if not song_id:
            raise ValueError("song_id is required")
            
        song = get_object_or_404(Song, id=song_id)
        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response_data(
                message="Song retrieved successfully",
                data=song.to_response_dataclass().__dict__
            )
        )

    @Common().exception_handler
    def delete_extract(self, request) -> Response:
        song_id = request.query_params.get('song_id')
        if not song_id:
            raise ValueError("song_id is required")
            
        song = get_object_or_404(Song, id=song_id)
        song.delete()
        
        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response_data(message="Song deleted successfully")
        )
