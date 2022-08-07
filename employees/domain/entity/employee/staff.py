from __future__ import annotations

from employees.domain.value_object.employee_profile import EmployeeProfile
from employees.domain.entity.employee._base_employee import BaseEmployeeEntity


class Staff(BaseEmployeeEntity):
    EMPLOYEE_TITLE = 'Staff'

    def __init__(self, employee_profile: EmployeeProfile):
        self._employee_profile: EmployeeProfile = employee_profile
