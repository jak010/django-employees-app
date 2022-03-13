from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import view as page
from . import controller as api

app_name = "customer"

urlpatterns = \
    [
        # Page
        path("page", page.sample.CustomerView.as_view()),

        # API
        path("", api.customer
             .CustomerListCreateAPIView.as_view()),  # GET: customer 목록 조회, POST : customer 생성
        path("<int:customerNumber>", api.customer
             .CustomerRetrieveUpdateDestroyAPIView.as_view(), name='detail')  # GET, PUT, DELETE

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
