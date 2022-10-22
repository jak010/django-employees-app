from django import forms

from employees.constant import EmployeeGenderType
from employees.exceptions import EmployeeDuplicationError
from employees.models.EmployeeModel import Employees


class EmployeeService:

    def create(self, employee_form: forms.Form) -> Employees:
        """ Employee 생성하기 """
        if not self.is_exist(emp_no=employee_form.cleaned_data['emp_no']):
            raise EmployeeDuplicationError()

        employee = Employees(
            emp_no=employee_form.cleaned_data['emp_no'],
            first_name=employee_form.cleaned_data['first_name'],
            last_name=employee_form.cleaned_data['last_name'],
            birth_date=employee_form.cleaned_data['birth_date'],
            hire_date=employee_form.cleaned_data['hire_date'],
            gender=EmployeeGenderType.with_value(value=employee_form.cleaned_data['gender'])
        )
        employee.save()

        return employee

    def is_exist(self, emp_no: int):
        """ employee가 존재하는치 체크함 """
        employee = Employees.objects.filter(emp_no=emp_no)
        if employee:
            return False
        return True
