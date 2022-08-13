from __future__ import annotations

import abc
from datetime import date
from enum import Enum


class EmployeeType(Enum):
    SENIOR_ENGINEER = 'Senior Engineer'
    ENGINEER = 'Engineer'
    ASSISTANT_ENGINEER = 'Assitant Engineer'

    STAFF = 'Staff'
    SENIOR_STAFF = 'Seniro Staff'

    TECHNIQUE_LEADER = 'Technique Leader'
    MANAGER = 'Manager'

    @classmethod
    def values(cls):
        return [e.value for e in cls]


class EmployeeGenderType(Enum):
    MAIL = "M"
    FEMAIL = "F"

    @classmethod
    def values(cls):
        return [e.value for e in cls]


class IEmployee(abc.ABC):
    """ Employee Interface """
    EMPLOYEE_TITLE = ''

    @abc.abstractmethod
    def __init__(self, employee_profile: EmployeeProfile):
        self.emp_no = employee_profile.emp_no
        self.first_name = employee_profile.first_name
        self.last_name = employee_profile.last_name
        self.hire_date = employee_profile.hire_date
        self.birth_date = employee_profile.birth_date
        self.gender = employee_profile.gender

    def __eq__(self, other: EmployeeProfile) -> bool:
        if self.emp_no == other.emp_no:
            return True
        return False

    def __hash__(self):
        return hash(str(self.emp_no) + self.EMPLOYEE_TITLE)

    def to_dict(self):
        return {
            'title': self.EMPLOYEE_TITLE,
            'emp_no': self.emp_no,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'hire_date': self.hire_date,
            'birth_date': self.birth_date,
            'gender': self.gender
        }


class EmployeeProfile:
    """ employee가 가져야 하는 data

    - employee model, title model의 data trasnaction object
    """

    def __init__(self,
                 emp_no: int,
                 first_name: str,
                 last_name: str,
                 hire_date: date,
                 birth_date: date,
                 gender: str,
                 title: str = None
                 ):
        self.title = title if title in EmployeeType.values() else None

        self.emp_no = emp_no
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.gender = gender

    @classmethod
    def with_kwargs(cls, **kwargs):
        return cls(
            title=kwargs.get('title', None),
            emp_no=kwargs.get('emp_no', None),
            first_name=kwargs.get('first_name', None),
            last_name=kwargs.get('last_name', None),
            hire_date=kwargs.get('hire_date', None),
            birth_date=kwargs.get('birth_date', None),
            gender=kwargs.get('gender', None)
        )
