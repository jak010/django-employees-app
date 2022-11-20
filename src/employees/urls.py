from django.urls import path

from .api.crud import (
    employees_list,
    employees_update,
    employees_detail,
    employees_create
)

app_name = "employee"

urlpatterns = [

    # EmployeesApi
    path("", employees_list.EmployeeListApi.as_view(), name='list'),
    path("create", employees_create.EmployeeCreateApi.as_view(), name='create'),
    path("<int:emp_no>/update", employees_update.EmployeeUpdateApi.as_view(), name='update'),
    path("<int:emp_no>/detail", employees_detail.EmployeeDetailApi.as_view(), name='detail')

]
