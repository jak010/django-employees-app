from __future__ import annotations

from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.views import APIView

from employees.models.EmployeeModel import Employees


class EmployeeUpdateApi(APIView):
    """ Employee Update Api """

    class InputSerializer(serializers.Serializer):  # noqa
        first_name = serializers.CharField(max_length=10, required=False)
        last_name = serializers.CharField(max_length=10, required=False)

    def put(self, request, emp_no: int):
        """ employee 업데이트 api """

        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        employee = Employees.objects.get(emp_no=emp_no)
        employee.first_name = serializer.data['first_name']
        employee.last_name = serializer.data['last_name']
        employee.save()

        return HttpResponse()
