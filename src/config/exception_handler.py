from __future__ import annotations

import json
import traceback

from rest_framework import status
from rest_framework.utils.encoders import JSONEncoder

from .exceptions import BadRequestError, NotFoundError, InternalServerError


class ExceptionHandlerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.content:
            # json.loads를 이용하여 browser에서 테스트할 경우 JSONDecodeError가 일어난다.
            response_content = json.dumps(response.content.decode(), cls=JSONEncoder)
        else:
            response_content = None

        # API에서 캐치하는 종류의 400에러들 처리
        if response.status_code == status.HTTP_400_BAD_REQUEST:
            return BadRequestError(exc_message=response_content).to_response()
        if response.status_code == status.HTTP_404_NOT_FOUND:
            return NotFoundError(exc_message=response_content).to_response()
        else:
            pass

        return response

    def process_exception(self, request, exception):  # noqa
        """ API에서 캐치하지 못한 500에러 처리 """

        exc_msg = traceback.format_exception(exception)
        print(''.join(exc_msg))

        if isinstance(exception, Exception):
            return InternalServerError(exc_message=exc_msg) \
                .to_response()
