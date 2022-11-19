from __future__ import annotations

from rest_framework import status
from rest_framework.exceptions import (
    APIException,
)

from config.exceptions import ApplicationException


class EmployeeException(ApplicationException):
    """ EmployeeExcetpion"""

    class EmployeeCreateFailError(APIException):
        """ Employee 생성 실패 """

    class EmployeeDuplicationError(APIException):
        """ 중복된 Employee """
        status_code = 200
        default_code = 10001
        default_detail = "Employee Duplicate, " + f"{default_code}"
