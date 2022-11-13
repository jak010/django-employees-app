from __future__ import annotations
from typing import TypedDict, Union
from rest_framework import status
from rest_framework.exceptions import (
    APIException,
)
from django.http.response import JsonResponse, HttpResponse


class HttpException:
    description: str
    status_code: status

    def __init__(self, exc_message: Union[str, list[str]]):
        self.exc_message = exc_message

    def to_response(self):
        return JsonResponse({
            'description': self.description,
            'detail': self.exc_message
        },
            status=self.status_code
        )


class InternalServerError(HttpException):
    description = "Internal Server Error"
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR


class BadRequestError(HttpException):
    description = "Bad Request Error"
    status_code = status.HTTP_400_BAD_REQUEST


class NotFoundError(HttpException):
    description = 'Not Found'
    status_code = status.HTTP_404_NOT_FOUND

    def to_response(self):
        return HttpResponse(
            status=self.status_code,
            content=self.exc_message
        )


class ApiException(Exception):
    """ All Exception Parser """


class EmployeeException(ApiException):
    """ EmployeeExcetpion"""

    class EmployeeCreateFailError(APIException):
        """ Employee 생성 실패 """

    class EmployeeDuplicationError(APIException):
        """ 중복된 Employee """
        status_code = 200
        default_code = 10001
        default_detail = "Employee Duplicate, " + f"{default_code}"
