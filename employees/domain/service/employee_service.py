from django import forms

from employees.domain.constant import EmployeeGenderType
from employees.domain.dto import EmployeeDto
from employees.domain.exception import EmployeeDuplicationError
from employees.domain.models.EmployeeModel import Employees


class EmployeeService:

    def create(self, employee_form: forms.Form):
        """ Employee 생성하기 """
        if not self._is_exist(emp_no=employee_form.cleaned_data['emp_no']):
            raise EmployeeDuplicationError()

        employee_dto = EmployeeDto(
            emp_no=employee_form.cleaned_data['emp_no'],
            first_name=employee_form.cleaned_data['first_name'],
            last_name=employee_form.cleaned_data['last_name'],
            birth_date=employee_form.cleaned_data['birth_date'],
            hire_date=employee_form.cleaned_data['hire_date'],
            gender=EmployeeGenderType.with_value(value=employee_form.cleaned_data['gender'])
        )

        return Employees.objects.create(**employee_dto.to_dict)

    def _is_exist(self, emp_no: int):
        """ employee가 존재하는치 체크함 """
        employee = Employees.objects.filter(emp_no=emp_no)
        if employee:
            return False
        return True

    def delete(self):
        return None

    def update(self):
        return None
