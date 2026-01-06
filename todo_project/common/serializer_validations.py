import json
import urllib.parse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from todo_project.common.utils import Utils
from todo_project.common.constants import Constants

class SerializerValidations:

    def __init__(self, serializer, exec_func: str = '', **kwargs):
        self.serializer = serializer
        self.exec_func = exec_func
        self.serializer_kwargs = kwargs

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            request: Request = args[0]

            data = Utils.get_query_params(request=request)
            if request.method in ["POST", "PUT", "PATCH"]:
                if hasattr(request, 'data') and request.data:
                    data.update(request.data)
                else: 
                    try:
                        parsed_info = urllib.parse.unquote(request.body.decode('utf-8').strip())
                        data.update(json.loads(parsed_info))
                    except Exception:
                         pass

            context = {"token_payload": getattr(request, "payload", {})}

            serializer = self.serializer(data=data, context=context, **self.serializer_kwargs)
            
            serializer._endpoint = request.path
            serializer._method = request.method

            validator_result = Utils.validator(serializer=serializer)
            
            if validator_result is True:
                try:
                     params = serializer.create(serializer.validated_data)
                except Exception:
                     params = serializer.validated_data
                
                request.params = params
                return func(*args, **kwargs)
            
            return Response(validator_result, status=status.HTTP_400_BAD_REQUEST)

        return wrapper

