from __future__ import annotations
from typing import TypedDict, Union
from rest_framework import status
from rest_framework.exceptions import (
    APIException,
)
from django.http.response import JsonResponse, HttpResponse


class BadRequestError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 40001
    default_detail = "Server Bad Request Error"


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
