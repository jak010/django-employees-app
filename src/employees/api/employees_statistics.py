from __future__ import annotations

from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.EmployeeModel import Employees
from ..serializers import EmployeeSerializer

from config.exceptions import NotFoundError


class EmployeeStatisticsApi(APIView):
    """ Employee Statistics Api
    - employee 통계
    """

    def get(self, request, emp_no: int): ...
