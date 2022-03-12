from typing import Protocol, NewType, Optional

from customer.domain.model import Customers


class CustomerRepository:
    model: Customers

    @property
    def model(self):
        return Customers

    def read(self):
        return self.model.objects.all()

    def find_by_pk(self, number: int) -> Optional[Customers]:
        customer = self.model.objects.get(pk=number)

        if customer is None:
            return None

        return customer
