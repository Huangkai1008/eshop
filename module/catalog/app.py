from fastapi import FastAPI, Request

from module.catalog.api.v1 import endpoint
from module.catalog.container import Container
from module.catalog.infrastructure.mapper import start_mappers


def create_app() -> FastAPI:
    container = Container()

    app = FastAPI()
    app.container = container  # type: ignore
    app.include_router(endpoint.router)

    @app.middleware('http')
    def resource_lifespan_middleware(request: Request, call_next):
        container.init_resources()
        response = call_next(request)
        container.shutdown_resources()
        return response

    start_mappers()
    return app
