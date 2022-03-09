from customer.domain import repository
from customer.models import Customers


class CustomerService:

    def __init__(self):
        self.repository = repository.CustomerRepository()

    def get_customer(self, number: int) -> Customers:
        return self.repository.find_by_pk(number=number)
