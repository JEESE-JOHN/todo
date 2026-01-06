from rest_framework import status
from rest_framework.response import Response
from django.core.paginator import Paginator

from features.music.models import Song
from features.music.serializers.response.song import SongResponseSerializer

from todo_project.common.utils import Utils

class MusicView:
    def create(self, params):
        song = Song.create(
            title=params.title,
            artist=params.artist
        )
        data = SongResponseSerializer(song).data
        return Response(Utils.success_response("Song created successfully", data), status=status.HTTP_201_CREATED)

    def get_all(self, params, request):
        page_num = int(params.page_num)
        limit = int(params.limit)

        qs = Song.get_all()

        # Filtering logic if needed (matching tasks/views.py structure)
        artist = params.artist
        if artist:
            qs = qs.filter(artist__icontains=artist)

        pages = Paginator(qs, limit)

        if pages.num_pages < page_num:
            return Response(
                status=status.HTTP_200_OK,
                data=Utils.error_response("Invalid page", "Page number exceeded")
            )

        page = pages.page(page_num)
        data = SongResponseSerializer(page.object_list, many=True).data

        full_path = ""
        try:
            full_path = request.get_full_path()
        except:
            pass

        data = Utils.add_page_parameter(
            final_data=data,
            page_num=page_num,
            total_page=pages.num_pages,
            total_count=pages.count,
            present_url=full_path,
            next_page_required=pages.num_pages != page_num
        )

        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response("Data fetched successfully", data)
        )

    def get_one(self, params):
        song_id = params.get("song_id")

        if not song_id:
            return Response(
                Utils.error_response("Validation error", "song_id is required"), status=status.HTTP_400_BAD_REQUEST)

        song = Song.get_one(int(song_id))
        if not song:
            return Response(
                Utils.error_response("Song not found", f"id {song_id} does not exist"), status=status.HTTP_200_OK)

        data = SongResponseSerializer(song).data
        return Response(Utils.success_response("Data fetched successfully", data), status=status.HTTP_200_OK)

    def update(self, song_id, params):
        song = Song.update(
            song_id,
            title=params.title,
            artist=params.artist
        )
        if not song:
            return Response(Utils.error_response("Song not found", f"id {song_id} does not exist"), status=status.HTTP_200_OK)
        data = SongResponseSerializer(song).data
        return Response(Utils.success_response("Song updated successfully", data), status=status.HTTP_200_OK)

    def delete(self, song_id):
        success = Song.delete_one(song_id)
        if not success:
            return Response(Utils.error_response("Song not found", f"id {song_id} does not exist"), status=status.HTTP_200_OK)
        return Response(Utils.success_response("Song deleted successfully"), status=status.HTTP_200_OK)
