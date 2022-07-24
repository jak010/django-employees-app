from django.test import TestCase, override_settings
from employees.models import Employees


# Create your tests here.

class EmployeesTestCase(TestCase):

    def setUp(self) -> None:
        self.test_emp_no = 10001

    def test_employee_data_loads(self):
        employee = Employees.objects.get(emp_no=self.test_emp_no)
        self.assertEqual(employee.emp_no, self.test_emp_no)
