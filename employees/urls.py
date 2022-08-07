from django.urls import path

from .views import employees

app_name = "employee"

urlpatterns = [

    # Post: Employee Create
    path("create", employees.EmployeeCreateApi.as_view(), name='create')

]
