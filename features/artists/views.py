from rest_framework import status
from rest_framework.response import Response
from django.core.paginator import Paginator

from features.artists.models import Artist
from features.artists.serializers.response.artist import ArtistResponseSerializer
from todo_project.common.utils import Utils

class ArtistView:
    def create(self, params):
        artist = Artist.create(
            song_id=params.song_id,
            bio=params.bio
        )
        data = ArtistResponseSerializer(artist).data
        return Response(Utils.success_response("Artist created successfully", data), status=status.HTTP_201_CREATED)

    def get_all(self, params, request):
        page_num = int(params.page_num)
        limit = int(params.limit)

        qs = Artist.get_all()

        song_id = params.song_id
        if song_id:
            qs = qs.filter(song_id=song_id)

        pages = Paginator(qs, limit)

        if pages.num_pages < page_num:
            return Response(
                status=status.HTTP_200_OK,
                data=Utils.error_response("Invalid page", "Page number exceeded")
            )

        page = pages.page(page_num)
        data = ArtistResponseSerializer(page.object_list, many=True).data

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
        artist_id = params.get("artist_id")

        if not artist_id:
            return Response(
                Utils.error_response("Validation error", "artist_id is required"), status=status.HTTP_400_BAD_REQUEST)

        artist = Artist.get_one(int(artist_id))
        if not artist:
            return Response(
                Utils.error_response("Artist not found", f"id {artist_id} does not exist"), status=status.HTTP_200_OK)

        data = ArtistResponseSerializer(artist).data
        return Response(Utils.success_response("Data fetched successfully", data), status=status.HTTP_200_OK)

    def update(self, artist_id, params):
        artist = Artist.update(
            artist_id,
            song_id=params.song_id,
            bio=params.bio
        )
        if not artist:
            return Response(Utils.error_response("Artist not found", f"id {artist_id} does not exist"), status=status.HTTP_200_OK)
        data = ArtistResponseSerializer(artist).data
        return Response(Utils.success_response("Artist updated successfully", data), status=status.HTTP_200_OK)

    def delete(self, artist_id):
        success = Artist.delete_one(artist_id)
        if not success:
            return Response(Utils.error_response("Artist not found", f"id {artist_id} does not exist"), status=status.HTTP_200_OK)
        return Response(Utils.success_response("Artist deleted successfully"), status=status.HTTP_200_OK)
