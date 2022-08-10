from __future__ import annotations

from employees.domain.entity.employee._base_employee import IEmployee, EmployeeType, EmployeeProfile


class AssistantEngineer(IEmployee):
    EMPLOYEE_TITLE = EmployeeType.ASSISTANT_ENGINEER.value

    def __init__(self, employee_profile: EmployeeProfile):
        super(AssistantEngineer, self).__init__(employee_profile=employee_profile)
