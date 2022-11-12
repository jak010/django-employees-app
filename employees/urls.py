from django.urls import path

from .api import (
    employee_create,
    employee_list,
    employee_update
)

app_name = "employee"

urlpatterns = [

    # Post: Employee Create
    path("create", employee_create.EmployeeCreateApi.as_view(), name='create'),
    path("", employee_list.EmployeeListApi.as_view(), name='list'),
    path("update", employee_update.EmployeeUpdateApi.as_view(), name='update')

]
