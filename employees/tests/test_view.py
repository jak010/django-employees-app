from django.test import TestCase
from django.test.client import Client
from django.shortcuts import reverse


class EmployeViewTest(TestCase):

    def setUp(self) -> None:
        self.client = Client()

    def test_employee_detail_view_with_exist_employee(self):
        exist_emp_no = 100001

        url = reverse('employee-detail', kwargs={"employee_id": exist_emp_no})

        response = self.client.get(url)
        response_data = response.json()

        # status code
        self.assertEqual(response.status_code, 200)

        # response key test
        self.assertTrue(response_data['emp_no'])
        self.assertTrue(response_data['birth_date'])
        self.assertTrue(response_data['first_name'])
        self.assertTrue(response_data['last_name'])
        self.assertTrue(response_data['gender'])
        self.assertTrue(response_data['hire_date'])

    def test_employee_detail_view_with_not_exist_employee(self):
        not_exist_emp_no = 1

        url = reverse('employee-detail', kwargs={"employee_id": not_exist_emp_no})

        response = self.client.get(url)
        response_data = response.json()

        # status code
        self.assertEqual(response.status_code, 404)

        # response key test
        self.assertTrue(not response_data)
