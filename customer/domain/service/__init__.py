from customer.domain import (
    model,
    repository
)


class CustomerService:

    def __init__(self):
        self.repository = repository.CustomerRepository()

    def get_customer(self, number: int) -> model.Customers:
        return self.repository.find_by_pk(number=number)
