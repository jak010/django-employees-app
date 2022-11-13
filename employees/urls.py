from django.urls import path

from .api import (
    employee_create,
    employee_list,
    employee_update
)

app_name = "employee"

urlpatterns = [
    path("create", employee_create.EmployeeCreateApi.as_view(), name='create'),
    path("", employee_list.EmployeeListApi.as_view(), name='list'),
    path("<int:emp_no>/update", employee_update.EmployeeUpdateApi.as_view(), name='update')

]
