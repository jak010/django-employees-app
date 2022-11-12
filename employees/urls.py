from django.urls import path

from .api import (
    employee_create,
    employee_update
)

app_name = "employee"

urlpatterns = [

    # Post: Employee Create
    path("create", employee_create.EmployeeCreateApi.as_view(), name='create'),
    path("update", employee_update.EmployeeUpdateApi.as_view(), name='update')

]
