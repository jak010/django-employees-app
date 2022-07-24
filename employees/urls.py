from django.urls import path

from .views import employees

urlpatterns = [

    # GET: Employee Detail View
    path("employee/<int:employee_id>", employees.get_employee_api, name='employee-detail')
]
