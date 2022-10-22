class EmployeeException(Exception):
    """ EmployeeExcetpion"""


class EmployeeCreateFailError(EmployeeException):
    """ Employee 생성 실패 """


class EmployeeDuplicationError(EmployeeException):
    """ 중복된 Employee """
