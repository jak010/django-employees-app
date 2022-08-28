import pytest
import datetime
from django.shortcuts import reverse


@pytest.mark.django_db
def test_employee_create_view_with_success(client):
    """ employee 생성에 대한 성공 케이스 """
    # given
    url = reverse('employee:create')
    _today = datetime.date.today().strftime("%Y-%m-%d")

    # when
    response = client.post(url, data={
        'emp_no': 1,
        'last_name': 'ja',
        'first_name': 'ko',
        'hire_date': _today,
        'birth_date': _today,
        'gender': "M"
    })

    # then
    assert response.status_code == 201


@pytest.mark.django_db
def test_employee_create_view_with_request_data_none(client):
    """ employee request 데이터가 유효하지 않은 경우 """

    # given
    url = reverse("employee:create")
    _today = datetime.date.today().strftime("%Y-%m-%d")

    # when
    response = client.post(url, data={
        'last_name': 'ja',
        'first_name': 'ko',
        'hire_date': _today,
        'birth_date': _today,
        'gender': "A"
    })

    # then
    assert response.status_code == 400
