from __future__ import annotations

from typing import Optional
from django.utils.functional import cached_property

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

from ..models import Employees

from employees.domain.models import Employees as EmployeesModel


class EmployeeFactory:
    def __init__(self, employee_profile: EmployeeProfile):
        self._employee_profile: EmployeeProfile = employee_profile

        self._create_count = 0

    @cached_property
    def create_employee(self):
        try:
            employee = Employees.objects.create(
                first_name=self._employee_profile.first_name,
                last_name=self._employee_profile.last_name,
                birth_date=self._employee_profile.birth_date,
                hire_date=self._employee_profile.hire_date,
                gender=self._employee_profile.gender,
            )
        except Exception as e:
            return None
        else:
            self._create_count += 1

        return employee

    def get_employee(self, employee: EmployeesModel) -> Optional[IEmployee]:
        """ polymorphic of employee"""

        # Engineer Type
        if employee.title == EmployeeType.ENGINEER.value:
            return Engineer(employee=employee)
        if self.create_employee.title == EmployeeType.ASSISTANT_ENGINEER.value:
            return AssistantEngineer(employee=self.create_employee)
        if self.create_employee.title == EmployeeType.SENIOR_ENGINEER.value:
            return SeniorEngineer(employee=self.create_employee)

        # Staff Type
        if self.create_employee.title == EmployeeType.STAFF.value:
            return Staff(employee=self.create_employee)
        if self.create_employee.title == EmployeeType.SENIOR_STAFF.value:
            return SeniorStaff(employee=self.create_employee)

        # Leader & Manager
        if self.create_employee.title == EmployeeType.TECHNIQUE_LEADER.value:
            return TechniqueLeader(employee=self.create_employee)
        if self.create_employee.title == EmployeeType.MANAGER.value:
            return Manager(employee=self.create_employee)

        return None
