import abc

from employees.domain.value_object.employee_profile import EmployeeProfile


class BaseEmployeeEntity(abc.ABC):
    EMPLOYEE_TITLE = ''

    @abc.abstractmethod
    def __init__(self, employee_profile: EmployeeProfile):
        self._employee_profile: EmployeeProfile = employee_profile
