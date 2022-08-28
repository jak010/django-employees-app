import pytest

from django import forms
from django.utils.datastructures import MultiValueDict
from employees.domain.models import Employees


def _today():
    import datetime
    _today = datetime.date.today().strftime("%Y-%m-%d")
    return _today


class InputEmplyoeeModelForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'


@pytest.mark.django_db
def test_create_employee_form():
    valid_request = MultiValueDict()
    valid_request['emp_no'] = 1
    valid_request['last_name'] = 'ja'
    valid_request['first_name'] = 'ko'
    valid_request['gender'] = 'M'
    valid_request['hire_date'] = _today()
    valid_request['birth_date'] = _today()

    employee_form = InputEmplyoeeModelForm(data=valid_request)

    assert employee_form.is_valid() is True


@pytest.mark.django_db
def test_create_emplyoee_invalid_field_01():
    # 특정 필드(first_name)가 없는 request에 대한 테스트
    valid_request = MultiValueDict()
    valid_request['emp_no'] = 1
    valid_request['last_name'] = 'ja'
    valid_request['gender'] = 'M'

    employee_form = InputEmplyoeeModelForm(data=valid_request)

    assert employee_form.is_valid() is False


@pytest.mark.django_db
def test_create_emplyoee_invalid_field_02():
    # 요구하는 필드보다 추가된 필드가 들어온 경우
    valid_request = MultiValueDict()
    valid_request['emp_no'] = 1
    valid_request['last_name'] = 'ja'
    valid_request['first_name'] = 'ko'
    valid_request['gender'] = 'M'
    valid_request['hire_date'] = _today()
    valid_request['birth_date'] = _today()
    valid_request['title'] = 'engineer'

    employee_form = InputEmplyoeeModelForm(data=valid_request)

    # TODO: 요구하는 form의 데이터 자체는 전부 존재하므로 맞는 케이스?
    assert employee_form.is_valid() is True
