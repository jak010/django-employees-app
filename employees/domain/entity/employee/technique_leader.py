from __future__ import annotations

from employees.domain.value_object.employee_profile import EmployeeProfile
from employees.domain.entity.employee._base_employee import BaseEmployeeEntity


class TechniqueLeader(BaseEmployeeEntity):
    EMPLOYEE_TITLE = 'Technique Leader'

    def __init__(self, employee_profile: EmployeeProfile):
        self._employee_profile: EmployeeProfile = employee_profile
