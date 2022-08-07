from employees.domain.entity.employee import BaseEmployeeEntity
from employees.domain.value_object.employee_name import EmployeeName
from employees.domain.value_object.employee_profile import EmployeeProfile
from .employee_factory import EmployeeFactory


class EmployeeService:

    def employee_profile(self, employee_profile) -> EmployeeProfile:
        return EmployeeProfile(
            emp_no=employee_profile['emp_no'],
            title=employee_profile['title'],
            name=EmployeeName(
                first_name=employee_profile['first_name'],
                last_name=employee_profile['last_name']
            ),
            hire_date=employee_profile['hire_date'],
            birth_date=employee_profile['birth_date']
        )

    def create(self, employee_profile: dict) -> BaseEmployeeEntity:
        employee_profile = self.employee_profile(employee_profile)

        employee = EmployeeFactory(employee_profile=employee_profile) \
            .get_employee()

        return employee
