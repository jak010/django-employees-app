from __future__ import annotations

from employees.domain.entity.employee._base_employee import IEmployee, EmployeeType, EmployeeProfile


class Staff(IEmployee):
    EMPLOYEE_TITLE = EmployeeType.STAFF.value

    def __init__(self, employee_profile: EmployeeProfile):
        super(Staff, self).__init__(employee_profile=employee_profile)
