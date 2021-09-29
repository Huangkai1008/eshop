from dataclasses import dataclass

import pytest

from seedwork.application import BaseModel, QueryModel
from seedwork.domain import Entity


@dataclass
class Sample(Entity):
    username: str
    password: str


class SampleModel(BaseModel):
    id: str
    username: str


class SampleQueryModel(QueryModel):
    ...


class TestModel:
    def test_create_model_from_entity(self) -> None:
        sample = Sample(username='user', password='password')

        model = SampleModel.from_entity(sample)

        assert model.username == 'user'
        assert not hasattr(model, 'password')

    @pytest.mark.parametrize(
        'data,expected',
        [
            pytest.param(
                dict(),
                dict(page=1, size=10),
                id='empty values',
            ),
            pytest.param(
                dict(page=2, size=20),
                dict(page=2, size=20),
                id='custom values',
            ),
        ],
    )
    def test_create_query_model_succeed(self, data: dict, expected: dict) -> None:
        query = SampleQueryModel(**data)

        assert query.model_dump() == expected

    @pytest.mark.parametrize(
        'data',
        [
            pytest.param(
                dict(page=-1, size=10),
                id='invalid page - negative',
            ),
            pytest.param(
                dict(page=0, size=10),
                id='invalid page - zero',
            ),
            pytest.param(
                dict(page=1, size=-10),
                id='invalid size - negative',
            ),
            pytest.param(
                dict(page=1, size=0),
                id='invalid size - zero',
            ),
        ],
    )
    def test_create_query_model_fails(self, data: dict) -> None:
        with pytest.raises(ValueError):
            SampleQueryModel(**data)
