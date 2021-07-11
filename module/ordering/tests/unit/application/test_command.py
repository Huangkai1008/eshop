from contextlib import nullcontext as does_not_raise

import pytest

from module.ordering.application.command.create_order import CreateOrder


class TestCreateOrderCommand:
    def test_create_order_command_succeeds(self, create_order_input: dict) -> None:
        with does_not_raise():
            CreateOrder(**create_order_input)

    def test_create_order_command_fails_if_card_expired(
        self,
        create_order_input_with_card_expiration_in_past: dict,
    ) -> None:
        with pytest.raises(ValueError):
            CreateOrder(**create_order_input_with_card_expiration_in_past)

    def test_create_order_command_fails_if_no_order_lines(
        self,
        create_order_input_with_no_order_lines: dict,
    ) -> None:
        with pytest.raises(ValueError):
            CreateOrder(**create_order_input_with_no_order_lines)
