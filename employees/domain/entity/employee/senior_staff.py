from __future__ import annotations

from employees.domain.entity.employee._base_employee import IEmployee, EmployeeType, EmployeeProfile


class SeniorStaff(IEmployee):
    EMPLOYEE_TITLE = EmployeeType.SENIOR_STAFF.value

    def __init__(self, employee_profile: EmployeeProfile):
        super(SeniorStaff, self).__init__(employee_profile=employee_profile)
