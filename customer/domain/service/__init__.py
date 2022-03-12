from django.utils.functional import cached_property

from customer.domain import (
    model,
    repository
)


class CustomerService:

    @cached_property
    def repository(self):
        return repository.CustomerRepository()

    @property
    def customers(self):
        return self.repository.read()

    def customer(self, number: int) -> model.Customers:
        return self.repository.find_by_pk(number=number)
