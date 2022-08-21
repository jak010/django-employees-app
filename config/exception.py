import json
import traceback

from django.http.response import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from employees.domain.exception import EmployeeException


class HandleBusiniessExceptionMiddleware(MiddlewareMixin):

    def process_exception(self, request, excetpion):
        if isinstance(excetpion, Exception):
            # 정의되지 않은 Excpetion은 HttpServerErrorResponse 포맷의 응답을 반환함
            return HttpServerErrorResponse()

        return request


class HttpServerErrorResponse(HttpResponse):
    status_code = 500
    content_type = 'application/json'

    def __init__(self):
        super(HttpServerErrorResponse, self).__init__(
            content=self._to_content,
            content_type=self.content_type
        )

    @property
    def _to_content(self):
        content = {
            "message": "Exception Caused!, Checked Bellow",
            "debug": self._get_traceback()
        }
        return json.dumps(content, indent=4, default=str)

    def _get_traceback(self):
        _tracback = traceback.format_exc().strip().split('\n')

        return _tracback
