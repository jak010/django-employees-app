from __future__ import annotations

from employees.domain.entity.employee._base_employee import IEmployee, EmployeeType


class TechniqueLeader(IEmployee):
    EMPLOYEE_TITLE = EmployeeType.TECHNIQUE_LEADER.value
