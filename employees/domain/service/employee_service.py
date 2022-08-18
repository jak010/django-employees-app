from typing import Type

from .employee_factory import EmployeeFactory
from employees.domain.entity.employee import IEmployee, EmployeeProfile

from ..models import Employees as EmployeeModel


class EmployeeService:

    def create_employee(self, employee_profile: EmployeeProfile) -> IEmployee:
        employee = EmployeeFactory(employee_profile=employee_profile).get_instance()

        print(self.find_employee_by(emp_no=employee.emp_no))

        return employee

    def find_employee_by(self, emp_no: int):
        return EmployeeModel.objects.get(emp_no=emp_no)
