from rest_framework import status
from rest_framework.response import Response
from todo_project.common.config import Configurations
from todo_project.common.constants import Constants
from todo_project.common.utils import Utils

class Common:
    def __init__(self, response_handler=None):
        self.db_error = "Database Error"
        self.error = "Something went wrong"
        self.response_handler = response_handler

    def exception_handler(self, func):
        def exceptions(*args, **kwargs):
            try:
                fun = func(*args, **kwargs)
                if self.response_handler and hasattr(fun, 'data'):
                     pass

                return fun

            except ValueError as e:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data=Utils.error_response_data(message='Value Error ' + str(e), error=[str(e)]))
            except Exception as e:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                data=Utils.error_response_data(message='Exception Error ' + Utils.env_exception_handler(str(e)),
                                                               error=[str(e)]))

        return exceptions
