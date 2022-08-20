from employees.domain.models.EmployeeModel import Employees

from django import forms

from employees.domain.dto import EmployeeDto, TitleDto
from employees.domain.models.EmployeeModel import Employees
from employees.domain.constant import EmployeeGenderType

from django.http.response import HttpResponse


class HttpNewEmployeeResponse(HttpResponse):
    status_code = 200

    def __init__(self, content: dict):
        super(HttpNewEmployeeResponse, self).__init__(content=content)


class EmployeeService:

    def create(self, employee: forms.Form):
        employee_dto = EmployeeDto(
            first_name=employee.cleaned_data['first_name'],
            last_name=employee.cleaned_data['last_name'],
            birth_date=employee.cleaned_data['birth_date'],
            hire_date=employee.cleaned_data['hire_date'],
            gender=EmployeeGenderType.with_value(value=employee.cleaned_data['gender'])
        )

        try:
            new_employee = Employees.objects.create(**employee_dto.to_dict)
        except Exception as e:
            raise Exception("Employee Create Failed : ")

        return new_employee

    def delete(self):
        return None

    def update(self):
        return None
