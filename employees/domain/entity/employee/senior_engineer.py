from __future__ import annotations

from employees.domain.entity.employee._base_employee import IEmployee, EmployeeType


class SeniorEngineer(IEmployee):
    EMPLOYEE_TITLE = EmployeeType.SENIOR_ENGINEER.value
