from typing import Protocol, NewType, Optional

from customer.domain import (
    model
)


class CustomerRepository:

    def find_by_pk(self, number: int) -> Optional[model.Customers]:
        customer = model.Customers.objects.get(pk=number)

        if customer is None:
            return None

        return customer
