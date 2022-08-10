from __future__ import annotations

from employees.domain.entity.employee._base_employee import EmployeeProfile, EmployeeType, IEmployee


class Engineer(IEmployee):
    EMPLOYEE_TITLE = EmployeeType.ENGINEER.value

    def __init__(self, employee_profile: EmployeeProfile):
        super(Engineer, self).__init__(employee_profile=employee_profile)
