from __future__ import annotations

from rest_framework import status
from rest_framework.exceptions import (
    APIException,
)


class ApplicationException(Exception):
    """ Api Level Exception Type """


class BadRequestError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 40001
    default_detail = "Server Bad Request Error"


class NotFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_code = 40004
    default_detail = "Server NotFound"
