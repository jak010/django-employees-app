from django import forms
from django.http import HttpResponseBadRequest, JsonResponse
from django.utils.functional import cached_property

from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response

from .. import services


class EmployeeCreateApi(APIView):
    """ Employee 생성 Api """

    class InputSerializer(serializers.Serializer):  # noqa
        emp_no = serializers.IntegerField(max_value=10)
        first_name = serializers.CharField(max_length=15)
        last_name = serializers.CharField(max_length=15)
        gender = serializers.ChoiceField(choices=('M', 'F'))
        birth_date = serializers.DateField()
        hire_date = serializers.DateField()

    def post(self, request):
        """ employee 생성 api """
        serializer = self.InputSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)

        new_emplopyee = services.create_employee(
            **serializer.data
        )

        return Response(data=new_emplopyee.to_dict())
