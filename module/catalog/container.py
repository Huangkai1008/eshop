from dependency_injector import containers, providers

from module.catalog.application.use_case import (
    CatalogBrandUseCase,
    CatalogTypeUseCase,
    CatalogUseCase,
)
from module.catalog.infrastructure.repository.catalog import CatalogRepository
from module.catalog.infrastructure.repository.catalog_brand import (
    CatalogBrandRepository,
)
from module.catalog.infrastructure.repository.catalog_type import CatalogTypeRepository
from seedwork.infrastructure.persistence.sqlalchemy import (
    get_session,
    get_session_factory,
)


class Core(containers.DeclarativeContainer):
    config = providers.Configuration()


class Infrastructure(containers.DeclarativeContainer):
    config = providers.Configuration()

    session_factory = providers.Singleton(
        get_session_factory,
        database_url=config.database_url,
    )

    session = providers.Resource(
        get_session,
        session_factory=session_factory,
    )

    catalog_repository = providers.Factory(
        CatalogRepository,
        session=session,
    )

    catalog_brand_repository = providers.Factory(
        CatalogBrandRepository,
        session=session,
    )

    catalog_type_repository = providers.Factory(
        CatalogTypeRepository,
        session=session,
    )


class ApplicationContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    core = providers.Container(Core, config=config)

    infrastructure = providers.Container(Infrastructure, config=config)

    wiring_config = containers.WiringConfiguration(
        modules=[
            'module.catalog.api.v1.catalog',
            'module.catalog.api.v1.catalog_brand',
            'module.catalog.api.v1.catalog_type',
        ],
    )

    catalog_use_case = providers.Factory(
        CatalogUseCase,
        repository=infrastructure.catalog_repository,
    )

    catalog_brand_use_case = providers.Factory(
        CatalogBrandUseCase,
        repository=infrastructure.catalog_brand_repository,
    )

    catalog_type_use_case = providers.Factory(
        CatalogTypeUseCase,
        repository=infrastructure.catalog_type_repository,
    )
