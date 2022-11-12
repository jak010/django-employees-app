from __future__ import annotations

import json
import traceback

from rest_framework import status

from .exceptions import internal_server_error, bad_request_error


class ExceptionHandlerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response_content = json.loads(response.content.decode())

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            return bad_request_error(exc_message=response_content)

        return response

    def process_exception(self, request, exception):  # noqa

        if isinstance(exception, Exception):
            return internal_server_error(
                exc_message=traceback.format_exception(exception)
            )
