from typing import Any, Optional, Dict, List, Union

class Utilities:
    
    @staticmethod
    def success_response_data(message: str, data: Optional[Union[Dict, List]] = None) -> Dict[str, Any]:
       
        response = {'status': True}
        
        if message is not None:
            response['message'] = message
            
        if data is not None:
            response['data'] = data
            
        return response

    @staticmethod
    def error_response_data(message: str, errors: Optional[Any] = None) -> Dict[str, Any]:
        """
        Standardized error response.
        Returns: { 'status': False, 'message': message, 'errors': errors }
        """
        response = {'status': False}
        
        if message is not None:
            response['message'] = message
            
        if errors is not None:
            response['errors'] = errors
            
        return response
