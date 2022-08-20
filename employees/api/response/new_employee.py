import json

from django.http.response import HttpResponse

from employees.api.response import EmployeeResponsCode
from employees.domain.models.EmployeeModel import Employees as EmployeesModel


class HttpNewEmployeeResponse(HttpResponse):
    status_code = EmployeeResponsCode.CREATED.value
    content_type = "application/json"

    def __init__(self, new_employee: EmployeesModel):
        self.employee: EmployeesModel = new_employee

        super(HttpNewEmployeeResponse, self).__init__(
            content=self._to_content,
            content_type=self.content_type

        )

    @property
    def _to_content(self):
        content = {
            "message": "Employee Was Created!",
            "data": {
                'emp_no': self.employee.emp_no,
                'first_name': self.employee.first_name,
                'last_name': self.employee.last_name,
                'gender': self.employee.gender,
                'birth_date': self.employee.birth_date,
                'hire_date': self.employee.hire_date
            }
        }
        return json.dumps(content)
