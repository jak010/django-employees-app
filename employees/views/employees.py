from django import forms
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.utils.functional import cached_property
from django.views.generic import View as _View

from ..domain.service.employee_service import EmployeeService


class EmployeeCreateApi(_View):
    class InputForm(forms.Form):
        title = forms.CharField(max_length=25)
        emp_no = forms.IntegerField()
        first_name = forms.CharField(max_length=15)
        last_name = forms.CharField(max_length=15)
        birth_date = forms.DateField()
        hire_date = forms.DateField()

    @cached_property
    def service(self):
        return EmployeeService()

    def post(self, request):
        employee = self.InputForm(data=request.POST)
        if not employee.is_valid():
            raise Exception("Invalid Request")

        new_employee = self.service.create(
            employee_profile=employee.cleaned_data
        )

        if new_employee is None:
            # 등록되지 않은 Employee 타입
            return HttpResponseBadRequest()  # 400

        return HttpResponse()  # 200
