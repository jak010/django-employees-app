from __future__ import annotations

from rest_framework import serializers

from .models.EmployeeModel import Employees, Titles


class TitlesSeializer(serializers.ModelSerializer):
    class Meta:
        model = Titles
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    titles_set = TitlesSeializer(many=True)

    class Meta:
        model = Employees
        fields = '__all__'
        extra_fields = 'titles_set'

    def to_representation(self, instance):
        return {
            'emp_no': instance.emp_no,
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'hire_date': instance.hire_date.isoformat(),
            'birth_date': instance.birth_date.isoformat(),
            'titles': [{
                'title_name': item.title,
                'from_date': item.from_date.isoformat(),
                'to_date': item.to_date.isoformat(),
            } for item in instance.titles_set.order_by('-to_date')]
        }
