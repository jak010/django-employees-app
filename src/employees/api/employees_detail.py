from __future__ import annotations

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.EmployeeModel import Employees


class EmployeeDetailApi(APIView):
    """ Employee Update Api """

    def get(self, request, emp_no: int):
        """ employee 업데이트 api """
        employee: Employees = Employees.objects.get(emp_no=emp_no)

        return Response(data=employee.to_dict())
