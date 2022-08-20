from django import forms
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.utils.functional import cached_property
from django.views.generic import View as _View

from ..domain.service.employee_service import EmployeeService


class EmployeeCreateApi(_View):
    """ Employee 생성 Api """

    @cached_property
    def service(self) -> EmployeeService:
        return EmployeeService()

    class InputEmployeeForm(forms.Form):
        first_name = forms.CharField(max_length=15)
        last_name = forms.CharField(max_length=15)
        gender = forms.CharField(max_length=1)
        birth_date = forms.DateField()
        hire_date = forms.DateField()

    def post(self, request):
        """ employee 생성 api """
        input_employee_form = self.InputEmployeeForm(data=request.POST)
        if not input_employee_form.is_valid():
            return HttpResponseBadRequest("InValid InputForm")  # 400

        self.service.create(input_employee_form)

        return HttpResponse()
