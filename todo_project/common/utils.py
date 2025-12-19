import random
import urllib.parse
from rest_framework.request import Request
from todo_project.common.constants import Constants
from todo_project.common.config import Configurations

class Utils:
    def __init__(self) -> None:
        super().__init__()
        self.validation_error = Constants.validation_error

    @staticmethod
    def success_response_data(message, data: list | dict = None, image=False):
        if image:
            return message
        if data is None and message is None:
            return {'status': True}
        if message is None:
            return {'status': True, 'data': data}
        if data is None:
            return {'status': True, 'message': message}
        return {'status': True, 'message': message, 'data': data}

    @staticmethod
    def error_response_data(message: str, error: list[str]|str|dict=None):
        return {'status': False, 'message': message, 'error': error}

    @staticmethod
    def conflict_response_data(message: str,error: list[str]):
        return{
            'status':False,
            'message':message,
            'error':error
        }

    @staticmethod
    def add_page_parameter(final_data: list | dict, page_num: int, total_page: int, total_count: int, present_url: str,
                           next_page_required: bool = False) -> dict:
        to_return = {'data': final_data,
                     'presentPage': page_num,
                     'totalPage': total_page,
                     'totalCount': total_count}
        if next_page_required and total_page > 1:
            if 'page_num' in present_url:
                to_return['nextPageUrl'] = present_url.replace('page_num=' + str(page_num),
                                                               'page_num=' + str(page_num + 1))
            else:
                if '?' in present_url:
                    params, base_url = Utils.extract_params(url=present_url)
                    present_url = base_url + '?' + '&'.join(params)
                    to_return['nextPageUrl'] = present_url + '&page_num=' + str(page_num + 1)
                else:
                    to_return['nextPageUrl'] = present_url + '?page_num=' + str(page_num + 1)
        return to_return

    @staticmethod
    def extract_params(url: str):
        query = url.split('?')
        if len(query) > 1:
            info = query[1]
            info = urllib.parse.unquote(info.strip())
        else:
            info = 'page_num=1'

        return info.split('&'), query[0]

    @staticmethod
    def get_query_params(request: Request):
        query_params = {}
        try:
            url = request.get_full_path()
        except:
            url = request.path
        query, base_url = Utils.extract_params(url=url)
        for i in query:
            try:
                key, value = i.split('=')
            except:
                key = i
                value = ''
            query_params[key] = value
        return query_params

    @staticmethod
    def env_exception_handler(message: str):
        if Configurations.debug:
            return message
        return Constants.server_error

    def validator(self, serializer) -> bool | dict:
        if serializer.is_valid() is False:
             # Just return validation failure, don't return Response directly here 
             # as cleaner pattern is to let caller handle it or return structure
            return Utils.error_response_data(message=self.validation_error, error=self.flatten_errors(serializer.errors))
        return True

    def flatten_errors(self, errors, parent_key=""):
        flat_errors = []

        if isinstance(errors, dict):
            for key, value in errors.items():
                field_name = str(key).replace("_", " ").title()
                full_key = f"{parent_key}.{field_name}" if parent_key else field_name
                flat_errors.extend(self.flatten_errors(value, parent_key=full_key))

        elif isinstance(errors, list):
            for item in errors:
                flat_errors.extend(self.flatten_errors(item, parent_key=parent_key))

        else:
            if parent_key:
                flat_errors.append(f"{parent_key}: {errors}")
            else:
                flat_errors.append(str(errors))

        return flat_errors
