from typing import Any, Callable

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError

from module.catalog.api.v1 import endpoint
from module.catalog.container import Container
from module.catalog.exception import (
    bad_request_handler,
    page_not_found_handler,
    server_error_handler,
    validation_exception_handler,
)
from module.catalog.infrastructure.mapper import start_mappers


def create_app() -> FastAPI:
    container = Container()

    app = FastAPI(
        title='Catalog API',
        description='Catalog API',
        version='0.1.0',
    )
    app.container = container  # type: ignore

    app.add_exception_handler(404, page_not_found_handler)
    app.add_exception_handler(400, bad_request_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(500, server_error_handler)

    app.include_router(endpoint.router)

    @app.middleware('http')
    def resource_lifespan_middleware(request: Request, call_next: Callable) -> Any:
        response = call_next(request)
        container.shutdown_resources()
        return response

    start_mappers()
    return app
