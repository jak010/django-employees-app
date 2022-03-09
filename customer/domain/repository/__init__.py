from typing import Protocol, NewType, Optional

import objects as objects

from customer.models import Customers


class CustomerRepository:

    def find_by_pk(self, number: int) -> Optional[Customers]:
        customer = Customers.objects.get(pk=number)

        if customer is None:
            return None

        return customer
