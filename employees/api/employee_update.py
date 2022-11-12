from django import forms
import uuid
from django.http import HttpResponseBadRequest, HttpResponse
from django.views.generic import View as _View

from config.type_defined import DjangoModelType
from ..models import Employees

from django.db import transaction


class EmployeeUpdateApi(_View):
    """ Employee Update Api """

    def post(self, request):
        """ employee 생성 api """
        model: DjangoModelType = Employees.objects.get(emp_no=5)

        with transaction.atomic():
            current_value = int(model.first_name)
            current_value = current_value + 1

            model.first_name = str(current_value)
            model.save()

        transaction.commit()
        return HttpResponse()
