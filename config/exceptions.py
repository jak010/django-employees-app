from __future__ import annotations

from rest_framework import status
from rest_framework.exceptions import APIException
from django.http.response import JsonResponse


def internal_server_error(exc_message):
    """
    Generic 500 error handler.
    """
    data = {
        'error': 'Internal Server Error',
        'exec': exc_message
    }
    return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
