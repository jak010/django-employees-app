from __future__ import annotations

from employees.domain.entity.employee._base_employee import IEmployee, EmployeeType


class SeniorStaff(IEmployee):
    EMPLOYEE_TITLE = EmployeeType.SENIOR_STAFF.value
