from __future__ import annotations

from typing import Optional

from ..entity.employee import (
    IEmployee,
    EmployeeProfile,
    EmployeeType,
    Engineer,
    AssistantEngineer,
    SeniorEngineer,
    Staff,
    SeniorStaff,
    TechniqueLeader,
    Manager
)


class EmployeeFactory:
    def __init__(self, employee_profile: EmployeeProfile):
        self._employee_profile: EmployeeProfile = employee_profile

    def get_instance(self) -> Optional[IEmployee]:

        if self._employee_profile.title is None:
            return None

        # Engineer Type
        if self._employee_profile.title == EmployeeType.ENGINEER.value:
            return Engineer(employee_profile=self._employee_profile)
        if self._employee_profile.title == EmployeeType.ASSISTANT_ENGINEER.value:
            return AssistantEngineer(employee_profile=self._employee_profile)
        if self._employee_profile.title == EmployeeType.SENIOR_ENGINEER.value:
            return SeniorEngineer(employee_profile=self._employee_profile)

        # Staff Type
        if self._employee_profile.title == EmployeeType.STAFF.value:
            return Staff(employee_profile=self._employee_profile)
        if self._employee_profile.title == EmployeeType.SENIOR_STAFF.value:
            return SeniorStaff(employee_profile=self._employee_profile)

        # Leader & Manager
        if self._employee_profile.title == EmployeeType.TECHNIQUE_LEADER.value:
            return TechniqueLeader(employee_profile=self._employee_profile)
        if self._employee_profile.title == EmployeeType.MANAGER.value:
            return Manager(employee_profile=self._employee_profile)
