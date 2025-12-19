import json
import urllib.parse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from todo_project.common.utils import Utils
from todo_project.common.constants import Constants

class SerializerValidations:

    def __init__(self, serializer, exec_func: str = '', **kwargs):
        self.validation_error = Constants.validation_error
        self.serializer = serializer
        self.exec_func = exec_func
        self.message = "Request added to queue"
        self.serializer_kwargs = kwargs

    def validate(self, func):
        def validator(*args, **kwargs):
            request: Request = args[0]

            if request.method in ["POST", "PUT", "PATCH"]:
                if hasattr(request, 'data') and request.data:
                    data = request.data
                else: 
                    try:
                        parsed_info = urllib.parse.unquote(request.body.decode('utf-8').strip())
                        data = json.loads(parsed_info)
                    except:
                         data = {}
            else:
                data = Utils.get_query_params(request=request)

            context = {"token_payload": getattr(request, "payload", {})}

            serializer = self.serializer(data=data, context=context, **self.serializer_kwargs)
            
            serializer._endpoint = request.path
            serializer._method = request.method

            validator_result = Utils().validator(serializer=serializer)
            
            if validator_result is True:
                try:
                     params = serializer.create(serializer.validated_data)
                except Exception as e:
                     params = serializer.validated_data
                
                request.params = params
                return func(*args, **kwargs)
            
            return Response(validator_result, status=status.HTTP_400_BAD_REQUEST)

        return validator
