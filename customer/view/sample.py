from django.shortcuts import render
from django.views.generic import TemplateView


class CustomerView(TemplateView):
    template_name = "customer/index.html"

    def get(self, request, *args, **kwargs):
        return render(
            request=request,
            template_name=self.template_name,
            context=self.get_context_data()
        )

    def get_context_data(self, **kwargs):
        return {"message": "Customers"}
