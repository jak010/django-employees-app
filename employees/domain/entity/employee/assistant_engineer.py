from __future__ import annotations

from employees.domain.entity.employee._base_employee import IEmployee, EmployeeType


class AssistantEngineer(IEmployee):
    EMPLOYEE_TITLE = EmployeeType.ASSISTANT_ENGINEER.value
