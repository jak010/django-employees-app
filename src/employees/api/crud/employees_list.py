from __future__ import annotations

import django_filters
from rest_framework import serializers
from rest_framework.views import APIView

from config.paginator import DefaultPaginator
from employees.models.EmployeeModel import Employees


class EmployeeListApi(APIView):
    """ Employee 조회 Api """

    class FilterSet(django_filters.FilterSet):
        emp_no = django_filters.NumberFilter()
        emp_no__gt = django_filters.NumberFilter(field_name="emp_no", lookup_expr="gt")
        emp_no__lt = django_filters.NumberFilter(field_name="emp_no", lookup_expr="lt")

        first_name = django_filters.CharFilter(field_name='first_name', lookup_expr='icontains')

        class Meta:
            model = Employees
            fields = {
                'emp_no': ["lt", "gt"],
                'first_name': []
            }

    class InputSerializer(serializers.Serializer):  # noqa
        emp_no = serializers.IntegerField(max_value=100000, required=False)
        emp_no__gt = serializers.IntegerField(max_value=100000, required=False)
        emp_no__lt = serializers.IntegerField(max_value=100000, required=False)

        first_name = serializers.CharField(max_length=10, required=False)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Employees
            fields = '__all__'

    def get(self, request):
        """ employee 목록조회 """

        # InputSerializer (In QueryParam)
        input_serializer = self.InputSerializer(data=request.query_params)
        input_serializer.is_valid(raise_exception=True)

        # Filter
        filter_set = self.FilterSet(
            input_serializer.validated_data,
            Employees.objects.all()
        )

        # paginaion
        paginator = DefaultPaginator()

        # Serialize
        items = self.OutputSerializer(
            paginator.paginate_queryset(queryset=filter_set.qs, request=self.request),
            many=True
        )

        return paginator.get_paginated_response(items.data)
