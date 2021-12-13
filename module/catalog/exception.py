import traceback
from typing import Any, Optional, Union

from fastapi.exceptions import HTTPException, RequestValidationError
from loguru import logger
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_500_INTERNAL_SERVER_ERROR,
)


class InvalidSystemClockException(Exception):
    ...


class GetHardwareIdFailedException(Exception):
    ...


class BadRequestException(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[dict] = None):
        super(BadRequestException, self).__init__(HTTP_400_BAD_REQUEST, detail, headers)


async def page_not_found_handler(_: Request, exc: HTTPException) -> JSONResponse:
    logger.warning(exc.detail)
    return JSONResponse(dict(message='Item not found'), status_code=exc.status_code)


async def bad_request_handler(_: Request, exc: BadRequestException) -> JSONResponse:
    logger.warning(exc.detail)
    return JSONResponse(dict(message=exc.detail), status_code=HTTP_400_BAD_REQUEST)


async def validation_exception_handler(
    _: Request, exc: Union[RequestValidationError, ValidationError]
) -> JSONResponse:
    errors = exc.errors()
    message = errors[0]['msg']
    logger.warning(errors)

    return JSONResponse(
        dict(message=message, detail=exc.errors()),
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
    )


async def server_error_handler(_: Request, __: HTTPException) -> JSONResponse:
    logger.error('SERVER ERROR')
    logger.warning(traceback.format_exc())
    return JSONResponse(
        dict(message='Server error'), status_code=HTTP_500_INTERNAL_SERVER_ERROR
    )
