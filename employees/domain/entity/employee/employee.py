from __future__ import annotations

from enum import Enum

from django.forms import Form


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


class EmployeeEntity:
    """ Employee Entity """

    def __init__(self, first_name, last_name, hire_date, birth_date, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.gender = gender

    @classmethod
    def with_form(cls, employee_form: Form):
        return cls(
            first_name=employee_form.cleaned_data['first_name'],
            last_name=employee_form.cleaned_data['last_name'],
            hire_date=employee_form.cleaned_data['hire_date'],
            birth_date=employee_form.cleaned_data['birth_date'],
            gender=employee_form.cleaned_data['gender']
        )
