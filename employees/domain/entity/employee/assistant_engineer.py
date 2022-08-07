from __future__ import annotations

from employees.domain.entity.employee._base_employee import BaseEmployeeEntity
from employees.domain.value_object.employee_profile import EmployeeProfile


class AssistantEngineer(BaseEmployeeEntity):
    EMPLOYEE_TITLE = 'Assistant Engineer'

    def __init__(self, employee_profile: EmployeeProfile):
        self._employee_profile: EmployeeProfile = employee_profile
