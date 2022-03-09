from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response

from ..domain.service import CustomerService
from ..domain.serializer import CustomerReadSerializer, CustomerCreateSerializer

from ..models import Customers


class CustomerListView(ListAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerReadSerializer


class CustomerCreateView(CreateAPIView):
    serializer_class = CustomerCreateSerializer

# class CustomerDetailView(APIView):
#
#     @property
#     def service(self):
#         return CustomerService()
#
#     def get(self, request, customer_number):
#         customer = self.service.get_customer(number=customer_number)
#
#         print(customer.customerNumber)
#
#         return Response(200)
