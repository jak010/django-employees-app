import json
import traceback

from django.utils.deprecation import MiddlewareMixin
from django.http.response import HttpResponseServerError
import traceback
from .exceptions import ApiException, internal_server_error


class ExceptionHandlerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def process_exception(self, request, exception):  # noqa
        if isinstance(exception, Exception):
            return internal_server_error(
                exc_message=traceback.format_exception(exception))
