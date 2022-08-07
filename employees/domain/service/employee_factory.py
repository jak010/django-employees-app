from __future__ import annotations

from typing import Optional

from ..entity.employee import (
    BaseEmployeeEntity,
    Engineer,
    AssistantEngineer,
    SeniorEngineer,
    Staff,
    SeniorStaff,
    TechniqueLeader,
    Manager
)
from ..value_object.employee_profile import EmployeeProfile


class EmployeeFactory:
    def __init__(self, employee_profile: EmployeeProfile):
        self._employee_profile: EmployeeProfile = employee_profile

    def get_employee(self) -> Optional[BaseEmployeeEntity]:

        # Engineer Type
        if self._employee_profile.title == Engineer.EMPLOYEE_TITLE:
            return Engineer(employee_profile=self._employee_profile)
        if self._employee_profile.title == AssistantEngineer.EMPLOYEE_TITLE:
            return AssistantEngineer(employee_profile=self._employee_profile)
        if self._employee_profile.title == SeniorEngineer.EMPLOYEE_TITLE:
            return SeniorEngineer(employee_profile=self._employee_profile)

        # Staff Type
        if self._employee_profile.title == Staff.EMPLOYEE_TITLE:
            return Staff(employee_profile=self._employee_profile)
        if self._employee_profile.title == SeniorStaff.EMPLOYEE_TITLE:
            return SeniorStaff(employee_profile=self._employee_profile)

        # Leader & Manager
        if self._employee_profile.title == TechniqueLeader.EMPLOYEE_TITLE:
            return TechniqueLeader(employee_profile=self._employee_profile)
        if self._employee_profile.title == Manager.EMPLOYEE_TITLE:
            return Manager(employee_profile=self._employee_profile)

        return None
