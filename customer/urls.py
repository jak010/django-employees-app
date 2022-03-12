from django.urls import path, include

from . import view as page
from . import controller as api

urlpatterns = [

    # Page
    path("page", page.sample.CustomerView.as_view()),

    # API
    path("", api.customer
         .CustomerListCreateAPIView.as_view()),  # GET: customer 목록 조회, POST : customer 생성
    path("<int:customerNumber>", api.customer
         .CustomerRetrieveUpdateDestroyAPIView.as_view())  # GET, PUT, DELETE

]
