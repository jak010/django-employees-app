from __future__ import annotations

import django_filters
from rest_framework import serializers
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView

from ..models.EmployeeModel import Employees


class EmployeeListApi(APIView):
    """ Employee 조회 Api """

    class LimitofPage(LimitOffsetPagination):
        default_limit = 10

    class QueryParamSerializer(serializers.Serializer):  # noqa
        emp_no = serializers.IntegerField(max_value=100000, required=False)
        emp_no__gt = serializers.IntegerField(max_value=100000, required=False)
        emp_no__lt = serializers.IntegerField(max_value=100000, required=False)

        first_name = serializers.CharField(max_length=10, required=False)

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

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Employees
            fields = '__all__'

    def get(self, request):
        """ employee 목록조회 """

        # Query
        query_params = self.QueryParamSerializer(data=request.query_params)
        query_params.is_valid(raise_exception=True)

        # Filter
        query_set = Employees.objects.all()
        filters = self.FilterSet(query_params.validated_data, query_set)

        # paginaion
        page = self.LimitofPage()
        p = page.paginate_queryset(queryset=filters.qs, request=self.request)

        # Serialized
        items = self.OutputSerializer(p, many=True)

        return page.get_paginated_response(items.data)
