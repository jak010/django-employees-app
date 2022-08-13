from .employee_factory import EmployeeFactory
from employees.domain.entity.employee import IEmployee, EmployeeProfile

from employees.domain.models import Employees as EmployeesModel
from typing import Optional
from django.http.response import HttpResponse


class EmployeeCreateError(HttpResponse):
    status_code = 200

    def __init__(self):
        """ Employee 생성 실패 """
        super(EmployeeCreateError, self).__init__(status=200_001)


class EmployeeService:

    def create(self, employee_profile: EmployeeProfile) -> Optional[EmployeesModel, HttpResponse]:
        """ employee 생성 """
        employee = EmployeeFactory(employee_profile=employee_profile) \
            .get_employee()

        if employee is None:
            return EmployeeCreateError()

        employee = EmployeesModel.objects.create(
            birth_date=employee.birth_date,
            first_name=employee.first_name,
            last_name=employee.last_name,
            gender=employee.gender,
            hire_date=employee.hire_date,
        )

        return employee
