from .employee_factory import EmployeeFactory
from employees.domain.entity.employee import IEmployee, EmployeeProfile


class EmployeeService:

    # def employee_profile(self, employee_profile) -> EmployeeProfile:
    #     return EmployeeProfile(
    #         emp_no=employee_profile['emp_no'],
    #         title=employee_profile['title'],
    #         name=EmployeeName(
    #             first_name=employee_profile['first_name'],
    #             last_name=employee_profile['last_name']
    #         ),
    #         hire_date=employee_profile['hire_date'],
    #         birth_date=employee_profile['birth_date']
    #     )

    def create(self, employee_profile: EmployeeProfile) -> IEmployee:
        # employee_profile = self.BaseEmployeeEntity(employee_profile)
        print('='*20)
        print(employee_profile.title)
        employee = EmployeeFactory(employee_profile=employee_profile) \
            .get_employee()

        print('=' * 20)

        return employee
