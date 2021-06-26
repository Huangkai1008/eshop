import uuid

from eshop.seedwork.domain.entity import Entity


class TestEntity:
    def test_entities_are_equal(self) -> None:
        entity1 = Entity()
        entity2 = Entity()
        entity1.id = entity2.id = str(uuid.uuid4())

        equality: bool = entity1 == entity2

        assert equality is True

    def test_entities_are_not_equal(self) -> None:
        entity1 = Entity()
        entity2 = Entity()

        equality: bool = entity1 == entity2

        assert equality is False
