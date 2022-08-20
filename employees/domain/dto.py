from datetime import date

import dataclasses

from .constant import EmployeeGenderType


@dataclasses.dataclass
class EmployeeDto:
    first_name: str
    last_name: str
    gender: EmployeeGenderType

    birth_date: date
    hire_date: date

    @property
    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "birth_date": self.birth_date,
            "hire_date": self.hire_date
        }


@dataclasses.dataclass
class TitleDto:
    title: str
    from_date: date
    to_date: date
