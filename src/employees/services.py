from __future__ import annotations

from django.db import IntegrityError

from .exceptions import EmployeeException
from .models.EmployeeModel import Employees


def create_employee(
        *,
        emp_no: int,
        first_name: str,
        last_name: str,
        gender,
        hire_date,
        birth_date
) -> Employees:
    try:
        model = Employees.objects.create(
            emp_no=emp_no,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            hire_date=hire_date,
            birth_date=birth_date
        )
    except IntegrityError as e:
        raise EmployeeException.EmployeeDuplicationError

    return model
