from django.urls import path, include

from .controller import (
    customer
)

from .view import (
    sample
)

urlpatterns = [
    path("page", sample.CustomerView.as_view()),

    # Controller Call
    path("", customer.CustomerListView.as_view())  # GET: 고객 목록조회

]
