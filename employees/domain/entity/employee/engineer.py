from __future__ import annotations

from employees.domain.entity.employee._base_employee import EmployeeType, IEmployee


class Engineer(IEmployee):
    EMPLOYEE_TITLE = EmployeeType.ENGINEER.value
