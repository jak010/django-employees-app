from rest_framework.generics import ListAPIView

from ..models import Customers
from ..serializer import CustomerReadSerializer


class CustomerListView(ListAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerReadSerializer
