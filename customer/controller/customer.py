from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from ..domain.model import (
    Customers
)

from ..domain.model.serializer import (
    CustomerSerializer,
)


class CustomerListCreateAPIView(ListCreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer
    lookup_url_kwarg = "customerNumber"
