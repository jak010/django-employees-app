from employees.domain.value_object.name import EmployeeName
from employees.domain.entity.employee._base_employee import BaseEmployee


class SeniorStaff(BaseEmployee):
    EMPLOYEE_TITLE = 'Senior Staff'

    def __init__(self, emp_no, emp_name: EmployeeName, birth_date, hire_date):
        super().__init__(emp_no, emp_name, birth_date, hire_date)
