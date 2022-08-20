from django.urls import path

from .api import (
    employee_create
)

app_name = "employee"

urlpatterns = [

    # Post: Employee Create
    path("create", employee_create.EmployeeCreateApi.as_view(), name='create')

]
