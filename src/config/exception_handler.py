from __future__ import annotations

import traceback

from rest_framework import status

from .exceptions import (
    BadRequestError,
)

from rest_framework.response import Response
from rest_framework.views import exception_handler

from rest_framework.exceptions import ValidationError


def exception_handler_func(exc, context):
    if isinstance(exc, ValidationError):
        exec = BadRequestError()

    response = exception_handler(exec, context)
    if response is not None:
        response.data['code'] = exec.get_codes()
        response.data['detail'] = exc.get_full_details()

    return response
