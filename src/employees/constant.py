from __future__ import annotations

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

    @classmethod
    def with_value(cls, value):
        for e in cls:
            if e.value == value:
                return e.value
