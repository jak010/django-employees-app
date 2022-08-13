from typing import Union

from django.http.response import HttpResponse

from employees.domain.entity.employee import EmployeeProfile, IEmployee
from employees.domain.module.employee_factory import EmployeeFactory


class EmployeeCreateError(HttpResponse):
    status_code = 200

    def __init__(self):
        """ Employee 생성 실패 """
        super(EmployeeCreateError, self).__init__(status=200_001)


class EmployeeService:

    def create(self, employee_profile: EmployeeProfile) -> Union[IEmployee, HttpResponse]:
        """ employee 생성 """
        employee_factory = EmployeeFactory(employee_profile=employee_profile)
        employee_factory.create_employee()

        employee = employee_factory.get_employee()

        if employee is None:
            return EmployeeCreateError()

        return employee
