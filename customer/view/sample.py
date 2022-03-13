from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.functional import cached_property

from ..domain import (
    service
)


class CustomerView(TemplateView):
    template_name = "page/index.html"

    @cached_property
    def service(self):
        return service.CustomerService()

    def get(self, request, *args, **kwargs):
        return render(
            request=request,
            template_name=self.template_name,
            context=self.get_context_data()
        )

    def get_context_data(self, **kwargs):
        return {
            "message": "Customers",
            "customers": self.service.customers
        }
