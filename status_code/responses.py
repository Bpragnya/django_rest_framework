from rest_framework.response import Response
from .status_codes import CustomStatusCodes

class CustomResponse(Response):
    def __init__(self, data=None, status=CustomStatusCodes.SUCCESS, headers=None, message=None):
        response_data = {
            "status_code": status, 
            "data": data,
        }
        if message:
            response_data["message"] = message
        super().__init__(data=response_data, status=status, headers=headers)

class CustomErrorResponse(Response):
    def __init__(self, data=None, status=CustomStatusCodes.ERROR, headers=None, message=None):
        response_data = {
            "status_code": status,  
            "error": data,
        }
        if message:
            response_data["message"] = message
        super().__init__(data=response_data, status=status, headers=headers)

class SuccessNoDataResponse(Response):
    def __init__(self, message=None, headers=None):
        response_data = {
            "status_code": CustomStatusCodes.NO_DATA_FOUND,
        }
        if message:
            response_data["message"] = message
        super().__init__(data=response_data, status=CustomStatusCodes.NO_DATA_FOUND, headers=headers)

class ValidationErrorResponse(Response):
    def __init__(self, errors=None, headers=None, message=None):
        response_data = {
            "status_code": CustomStatusCodes.INVALID_DATA,
            "errors": errors,
        }
        if message:
            response_data["message"] = message
        super().__init__(data=response_data, status=CustomStatusCodes.INVALID_DATA, headers=headers)

class NotFoundResponse(Response):
    def __init__(self, message=None, headers=None):
        response_data = {
            "status_code": CustomStatusCodes.NO_DATA_FOUND,
        }
        if message:
            response_data["message"] = message
        super().__init__(data=response_data, status=CustomStatusCodes.NO_DATA_FOUND, headers=headers)
