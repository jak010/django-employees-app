from __future__ import annotations

from employees.domain.entity.employee._base_employee import IEmployee, EmployeeType


class Manager(IEmployee):
    EMPLOYEE_TITLE = EmployeeType.MANAGER.value
