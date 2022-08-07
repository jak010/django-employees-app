from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from .employee_name import EmployeeName


@dataclass
class EmployeeProfile:
    emp_no: int
    title: str
    name: EmployeeName
    hire_date: date
    birth_date: date

    def __eq__(self, other: EmployeeProfile) -> bool:
        if self.emp_no == other.emp_no:
            return True
        return False

    def __hash__(self):
        return hash(str(self.emp_no) + self.title)
