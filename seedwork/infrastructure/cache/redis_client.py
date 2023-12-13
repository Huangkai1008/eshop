from dataclasses import dataclass, field
from functools import partial
from typing import Any, Final, Optional

from redis import RedisCluster, Sentinel, StrictRedis

from seedwork.infrastructure.exception import InfraException
from seedwork.infrastructure.logging import Logger

REDIS_DEFAULT_CONN_NAME: Final[str] = 'redis_default'


@dataclass
class RedisClient:
    logger: Logger

    redis_url: str
    redis_password: Optional[str]
    redis_sentinel_nodes: Optional[list[str]]
    redis_cluster_nodes: Optional[list[str]]

    redis_conn_name: Optional[str] = REDIS_DEFAULT_CONN_NAME
    redis_sentinel_connect_args: dict = field(
        default_factory=lambda: dict(service_name='mymaster')
    )

    def get(self, key: str) -> Any:
        return self.client.get(key)

    def set(self, key: str, value: Any) -> Any:
        return self.client.set(key, value)

    def delete(self, key: str) -> bool:
        if not self.client.exists(key):
            return False

        self.client.delete(key)
        return True

    def __post_init__(self) -> None:
        connection_kwargs: dict = dict(
            socket_timeout=0.5, retry_on_timeout=True, socket_keepalive=True
        )
        if password := self.redis_password:
            connection_kwargs['password'] = password

        if redis_cluster_nodes := self.redis_cluster_nodes:
            self._init_redis_cluster_connection(redis_cluster_nodes, connection_kwargs)
        elif redis_sentinel_nodes := self.redis_sentinel_nodes:
            self._init_redis_sentinel_connection(
                redis_sentinel_nodes, connection_kwargs
            )
        else:
            self._init_redis_connection(self.redis_url, connection_kwargs)

        self.logger.log(f'Initializing redis hook for conn_name {self.redis_conn_name}')
        self._detect_connectivity()

    def _init_redis_cluster_connection(
        self, redis_cluster_nodes: list[str], connection_kwargs: dict
    ) -> None:
        startup_nodes = self._get_redis_cluster_startup_nodes(redis_cluster_nodes)
        client = partial(RedisCluster, startup_nodes, **connection_kwargs)
        self.client = client(decode_responses=True)
        self.raw_client = client()

    @classmethod
    def _get_redis_cluster_startup_nodes(
        cls, redis_cluster_nodes: list[str]
    ) -> list[dict]:
        start_up_nodes = []
        for node in redis_cluster_nodes:
            host, port = node.split(':')
            start_up_nodes.append(dict(host=host, port=port))
        return start_up_nodes

    def _init_redis_sentinel_connection(
        self, redis_sentinel_nodes: list[str], connection_kwargs: dict
    ) -> None:
        sentinels = self._get_redis_sentinel_nodes(redis_sentinel_nodes)
        client = partial(Sentinel, sentinels, **connection_kwargs)
        service_name = self.redis_sentinel_connect_args['service_name']
        self.client = client(decode_responses=True).master_for(service_name)
        self.raw_client = client().master_for(service_name)

    @staticmethod
    def _get_redis_sentinel_nodes(sentinel_nodes: list[str]) -> list[tuple[str, str]]:
        start_up_nodes = []
        for node in sentinel_nodes:
            host, port = node.split(':')
            start_up_nodes.append((host, port))
        return start_up_nodes

    def _init_redis_connection(self, redis_url: str, connection_kwargs: dict) -> None:
        client = partial(StrictRedis.from_url, redis_url, **connection_kwargs)
        self.client = client(decode_responses=True)
        self.raw_client = client()

    def _detect_connectivity(self) -> None:
        try:
            self.client.ping()
        except ConnectionError:
            raise InfraException('Redis connection error')
