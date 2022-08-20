import logging

from django import forms
import traceback
from employees.domain.constant import EmployeeGenderType
from employees.domain.dto import EmployeeDto
from employees.domain.models.EmployeeModel import Employees

from employees.domain.exception import EmployeeCreateFailError

from django.db.utils import DataError, IntegrityError


class EmployeeService:

    @staticmethod
    def create(employee_form: forms.Form):

        employee_dto = EmployeeDto(
            emp_no=employee_form.cleaned_data['emp_no'],
            first_name=employee_form.cleaned_data['first_name'],
            last_name=employee_form.cleaned_data['last_name'],
            birth_date=employee_form.cleaned_data['birth_date'],
            hire_date=employee_form.cleaned_data['hire_date'],
            gender=EmployeeGenderType.with_value(value=employee_form.cleaned_data['gender'])
        )

        try:
            new_employee = Employees.objects.create(**employee_dto.to_dict)
        except DataError as e:
            raise EmployeeCreateFailError()

        return new_employee

    def delete(self):
        return None

    def update(self):
        return None
