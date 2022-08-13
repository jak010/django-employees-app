from django import forms
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.utils.functional import cached_property
from django.views.generic import View as _View

from ..domain.entity.employee._base_employee import EmployeeProfile
from ..domain.service.employee_service import EmployeeService


class EmployeeCreateApi(_View):
    """ Employee 생성 Api """

    class InputEmployeeProfileForm(forms.Form):
        title = forms.CharField(max_length=25)
        emp_no = forms.IntegerField()
        first_name = forms.CharField(max_length=15)
        last_name = forms.CharField(max_length=15)
        gender = forms.CharField(max_length=1)
        birth_date = forms.DateField()
        hire_date = forms.DateField()

        @property
        def to_dict(self) -> EmployeeProfile:
            return EmployeeProfile.with_kwargs(**self.cleaned_data)

    @cached_property
    def service(self):
        return EmployeeService()

    def post(self, request):
        """ employee 생성 api """
        employee_profile = self.InputEmployeeProfileForm(data=request.POST)
        if not employee_profile.is_valid():
            return HttpResponseBadRequest("InValid InputForm")  # 400

        new_employee = self.service.create(
            employee_profile=employee_profile.to_dict
        )

        if new_employee is None:
            # 등록되지 않은 Employee 타입
            return HttpResponseBadRequest("InValid Employee Type")  # 400

        return HttpResponse()  # 200
