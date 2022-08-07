from __future__ import annotations

from employees.domain.entity.employee._base_employee import BaseEmployeeEntity
from employees.domain.value_object.employee_profile import EmployeeProfile


class Manager(BaseEmployeeEntity):
    EMPLOYEE_TITLE = 'Manager'

    def __init__(self, employee_profile: EmployeeProfile):
        self._employee_profile: EmployeeProfile = employee_profile
