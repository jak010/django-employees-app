from django.http.response import JsonResponse

from ..models import Employees


def get_employee_api(request, employee_id: int):
    try:
        employee = Employees.objects.get(emp_no=employee_id)
    except Employees.DoesNotExist:
        return JsonResponse(status=404, data={})

    return JsonResponse(
        status=200,
        data=employee.to_dict()
    )
