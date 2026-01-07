from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, OpenApiResponse
from rest_framework import status

from todo_project.common.serializers.response.failure import FailureResponseSerializer
from todo_project.common.serializers.response.success import SuccessResponseSerializer

class SwaggerPage:
    @staticmethod
    def get_all_parameters(exclude: set[str] = None):
        exclude = exclude or set()

        parameters = [
            OpenApiParameter(
                name="page_num",
                description="Page number to get the list of records",
                required=False,
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name="limit",
                description="Number of data in a single page",
                required=False,
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                default=10,
            ),
        ]

        return [p for p in parameters if p.name not in exclude]

    @staticmethod
    def get_parameters(names: list[str]):
        return [
            OpenApiParameter(name=name, description=f"{name} required",
                             required=True, type=OpenApiTypes.STR,
                             location=OpenApiParameter.QUERY)
            for name in names
        ]

    @staticmethod
    def response(description: str = None, response=None):
        resp = {
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                description="Bad Request",
                response=FailureResponseSerializer()
            ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                description="Unauthorized Access",
                response=FailureResponseSerializer()
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                description="Internal Server Error",
                response=FailureResponseSerializer()
            )
        }

        if response is not None:
            resp[status.HTTP_200_OK] = OpenApiResponse(response=response, description=description)
        elif description is not None:
            resp[status.HTTP_200_OK] = OpenApiResponse(
                description=description,
                response=SuccessResponseSerializer()
            )
        
        return resp
