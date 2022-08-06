import abc
from employees.domain.value_object.name import EmployeeName


class BaseEmployee(abc.ABC):
    EMPLOYEE_TITLE = ''

    def __init__(self, emp_no, emp_name: EmployeeName, birth_date, hire_date):
        self._emp_no: int = emp_no
        self._emp_name: EmployeeName = emp_name
        self._birth_date = birth_date
        self._hire_date = hire_date
