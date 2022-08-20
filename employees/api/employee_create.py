from django import forms
from django.utils.functional import cached_property
from django.views.generic import View as _View

from employees.api.response import HttpEmployeeInvalidInputResponse, HttpEmployeeServerErrorResponse

from employees.api.response.new_employee import HttpNewEmployeeResponse
from ..domain.service.employee_service import EmployeeService

from employees.domain.exception import EmployeeCreateFailError


class EmployeeCreateApi(_View):
    """ Employee 생성 Api """

    @cached_property
    def employee_service(self) -> EmployeeService:
        return EmployeeService()

    class InputEmployeeForm(forms.Form):
        emp_no = forms.IntegerField()
        first_name = forms.CharField(max_length=15)
        last_name = forms.CharField(max_length=15)
        gender = forms.ChoiceField(choices=(('M', 'M'), ('F', 'F')))
        birth_date = forms.DateField()
        hire_date = forms.DateField()

    def post(self, request):
        """ employee 생성 api """
        input_employee_form = self.InputEmployeeForm(data=request.POST)
        if not input_employee_form.is_valid():
            return HttpEmployeeInvalidInputResponse()

        # TODO: 데이터 생성시 발생할 수 있는 Exception은 무엇이 있을까?
        try:
            new_employee = self.employee_service.create(employee_form=input_employee_form)
        except EmployeeCreateFailError as e:
            return HttpEmployeeServerErrorResponse(error=str(e))  # TODO: Exception Handler?

        return HttpNewEmployeeResponse(new_employee=new_employee)
