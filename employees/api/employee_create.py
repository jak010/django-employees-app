from django import forms
from django.utils.functional import cached_property
from django.views.generic import View as _View
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse

from employees.api.error.duplicate_employee_error import DuplicateEmployeeResponseError
from employees.exceptions import EmployeeDuplicationError
from employees.service.employee_service import EmployeeService


class EmployeeCreateApi(_View):
    """ Employee 생성 Api """

    @cached_property
    def employee_service(self) -> EmployeeService:
        return EmployeeService()

    class InputEmployeeForm(forms.Form):
        emp_no = forms.IntegerField(required=True)
        first_name = forms.CharField(max_length=15, required=True)
        last_name = forms.CharField(max_length=15, required=True)
        gender = forms.ChoiceField(choices=(('M', 'M'), ('F', 'F')), required=True)
        birth_date = forms.DateField(required=True)
        hire_date = forms.DateField(required=True)

    def post(self, request):
        """ employee 생성 api """
        input_employee_form = self.InputEmployeeForm(data=request.POST)
        if not input_employee_form.is_valid():
            return HttpResponseBadRequest()

        try:
            new_employee = self.employee_service.create(
                employee_form=input_employee_form
            )
        except EmployeeDuplicationError as e:
            return DuplicateEmployeeResponseError()


        return JsonResponse(
            data=new_employee.to_dict()
        )
