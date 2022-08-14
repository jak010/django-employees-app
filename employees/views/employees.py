from django import forms
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.utils.functional import cached_property
from django.views.generic import View as _View

from ..domain.entity.employee import EmployeeEntity
from ..domain.service.employee_service import EmployeeService


class EmployeeCreateApi(_View):
    """ Employee 생성 Api """

    class InputForm(forms.Form):
        first_name = forms.CharField(max_length=15)
        last_name = forms.CharField(max_length=15)
        gender = forms.CharField(max_length=1)
        birth_date = forms.DateField()
        hire_date = forms.DateField()

    @cached_property
    def service(self):
        return EmployeeService()

    def post(self, request):
        """ employee 생성 api """
        input_form = self.InputForm(data=request.POST)
        if not input_form.is_valid():
            return HttpResponseBadRequest("InValid InputForm")  # 400

        new_employee = EmployeeEntity.with_form(employee_form=input_form)

        new_employee = self.service.create(employee=new_employee)

        return HttpResponse(
            content={
                'employee': new_employee.to_dict
            }
        )
