from __future__ import annotations

from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.EmployeeModel import Employees
from ..serializers import EmployeeSerializer


class EmployeeDetailApi(APIView):
    """ Employee Update Api """

    def get(self, request, emp_no: int):
        """ employee 상세조회 api """

        employee = Employees.objects.filter(emp_no=emp_no) \
            .first()

        # prefetch_related가 아닌 DRF Serializer에서 쿼리를 수행한다.
        serializer = EmployeeSerializer(employee)

        return Response(data=serializer.data)
