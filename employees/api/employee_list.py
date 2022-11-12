from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from .. import services

from ..models.EmployeeModel import Employees


class EmployeeListApi(APIView):
    """ Employee 조회 Api """

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Employees
            fields = '__all__'

    def get(self, request):
        query = Employees.objects.all().filter(emp_no__lt=15000)

        users = self.OutputSerializer(query, many=True).data

        return Response(users)
