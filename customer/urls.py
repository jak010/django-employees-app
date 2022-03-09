from django.urls import path, include

from .controller import (
    customer
)

from .view import (
    sample
)

urlpatterns = [
    path("page", sample.CustomerView.as_view()),

    # Controller
    # path("<int:customer_number>", customer.CustomerDetailView.as_view()),

    # Controller Call
    path("", customer.CustomerListView.as_view()),  # GET: customer 목록 조회
    path("create", customer.CustomerCreateView.as_view())  # POST : customer 생성

]
