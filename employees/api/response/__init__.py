import enum
import json

from django.http.response import HttpResponse
from typing import Union
import traceback


class EmployeeResponsCode(enum.Enum):
    OK = 200
    CREATED = 201
    NO_CONTENT = 204

    BAD_REQUEST = 400

    SERVER_ERROR = 500


class HttpEmployeeInvalidInputResponse(HttpResponse):
    status_code = EmployeeResponsCode.BAD_REQUEST.value
    content_type = "application/json"

    def __init__(self):
        super(HttpEmployeeInvalidInputResponse, self).__init__(
            content=self._to_content,
            content_type=self.content_type
        )

    @property
    def _to_content(self):
        content = {
            "messages": "Invalid Input Request !",
            "error": {}
        }
        return json.dumps(content)


class HttpEmployeeServerErrorResponse(HttpResponse):
    status_code = EmployeeResponsCode.SERVER_ERROR.value

    content_type = "application/json"

    def __init__(self, error: Union[dict, str]):
        self._error = error

        super(HttpEmployeeServerErrorResponse, self).__init__(
            content=self._to_content,
            content_type=self.content_type
        )

    @property
    def _to_content(self):
        content = {
            "message": "Exception Caused!, Checked Bellow",
            "error": str(traceback.format_exc())
        }

        return json.dumps(content, indent=4, default=str)
