from __future__ import annotations

import traceback

from rest_framework import status

from .exceptions import (
    BadRequestError,
    NotFoundError,
    InternalServerError
)


class ExceptionHandlerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response_content = response.content.decode()

        if response_content:
            if response.status_code == status.HTTP_400_BAD_REQUEST:
                return BadRequestError(exc_message=response_content).to_response()
            if response.status_code == status.HTTP_404_NOT_FOUND:
                return NotFoundError(exc_message=response_content).to_response()

        return response

    def process_exception(self, request, exception):  # noqa
        """ API에서 캐치하지 못한 500에러 """
        exc_msg = traceback.format_exception(exception)
        print(''.join(exc_msg))

        if isinstance(exception, Exception):
            return InternalServerError(exc_message=exc_msg) \
                .to_response()
