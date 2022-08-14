from typing import Union, Optional

from django.http.response import HttpResponse

from ..entity.employee import EmployeeEntity
from ..models import Employees as EmployeesModel


class EmployeeCreateError(HttpResponse):
    status_code = 200

    def __init__(self):
        """ Employee 생성 실패 """
        super(EmployeeCreateError, self).__init__(status=200_001)


class EmployeeService:

    def create(self, employee: EmployeeEntity) -> Optional[EmployeesModel, HttpResponse]:
        """ employee 생성하기 """

        try:
            employee = EmployeesModel.objects.create(
                birth_date=employee.birth_date,
                hire_date=employee.hire_date,
                first_name=employee.first_name,
                last_name=employee.last_name,
                gender=employee.gender,
            )
        except Exception:
            return EmployeeCreateError()

        return employee
