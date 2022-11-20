from __future__ import annotations

from django.db import IntegrityError

from .exceptions import EmployeeException
from .models.EmployeeModel import Employees
from django.db import transaction


def create_employee(
        *,
        first_name: str,
        last_name: str,
        gender,
        hire_date,
        birth_date
) -> Employees:
    last_row = Employees.manager.last_emp_no()

    try:
        with transaction.atomic():
            model = Employees.objects.create(
                emp_no=last_row + 1,
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                hire_date=hire_date,
                birth_date=birth_date
            )
    except IntegrityError:
        raise EmployeeException.EmployeeDuplicationError()
    finally:
        transaction.commit()

    return model


# TODO: 22/11/20, employees 통계 구현하기
def statistics_employees(): ...
