from dependency_injector import containers, providers

from module.catalog.application.use_case import CatalogUseCase
from module.catalog.infrastructure.repository.catalog import CatalogRepository
from seedwork.infrastructure.persistence.sqlalchemy import (
    get_session,
    get_session_factory,
)


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=['module.catalog.api.v1.endpoint'],
    )

    config = providers.Configuration()

    session_factory = providers.Singleton(
        get_session_factory,
        database_url='mysql+pymysql://root:12345678@localhost:3306/catalog',
    )

    session = providers.Resource(
        get_session,
        session_factory=session_factory,
    )

    catalog_repository = providers.Factory(
        CatalogRepository,
        session=session,
    )

    catalog_use_case = providers.Factory(
        CatalogUseCase,
        repository=catalog_repository,
    )
