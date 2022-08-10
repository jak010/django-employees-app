from __future__ import annotations

from employees.domain.entity.employee._base_employee import IEmployee, EmployeeType, EmployeeProfile


class Manager(IEmployee):
    EMPLOYEE_TITLE = EmployeeType.MANAGER.value

    def __init__(self, employee_profile: EmployeeProfile):
        super(Manager, self).__init__(employee_profile=employee_profile)
