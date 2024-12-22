from rest_framework import status
 
class CustomStatusCodes:
    SUCCESS = 200
    INVALID_DATA = 400
    ERROR = 500
    NO_DATA_FOUND = 201
    BAD_REQUEST=400
    INTERNAL_SERVER_ERROR = 501
    DUPLICATE_DATA=409

HTTP_STATUS = status

