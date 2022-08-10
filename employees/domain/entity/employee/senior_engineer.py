from __future__ import annotations

from employees.domain.entity.employee._base_employee import IEmployee, EmployeeType, EmployeeProfile


class SeniorEngineer(IEmployee):
    EMPLOYEE_TITLE = EmployeeType.SENIOR_ENGINEER.value

    def __init__(self, employee_profile: EmployeeProfile):
        super(SeniorEngineer, self).__init__(employee_profile=employee_profile)
