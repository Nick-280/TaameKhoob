"""Tests for OrderBuilder (Fluent API)."""

import sys
import os

sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
)

from taamekhoob.order.builder import OrderBuilder
from taamekhoob.menu.concrete_items import Espresso, PizzaMargherita


def test_builder_add_item():
    """test: add_item bayad item ro be sefaresh ezafe kone."""
    builder = OrderBuilder()
    pizza = PizzaMargherita("M")

    builder.add_item(pizza, qty=2)
    order = builder.build()

    assert len(order.items) == 1
    assert order.items[0][0] == pizza
    assert order.items[0][1] == 2


def test_builder_with_coupon():
    """test: with_coupon bayad code takhfif ro zakhire kone."""
    order = OrderBuilder().add_item(Espresso()).with_coupon("DISCOUNT20").build()

    assert order.coupon == "DISCOUNT20"


def test_builder_deliver_to():
    """test: deliver_to bayad address ro zakhire kone."""
    order = (
        OrderBuilder().add_item(Espresso()).deliver_to("Tehran, Valiasr St.").build()
    )

    assert order.address == "Tehran, Valiasr St."


def test_builder_pay_with():
    """test: pay_with bayad gateway ro zakhire kone."""
    order = OrderBuilder().add_item(Espresso()).pay_with("zarinpal").build()

    assert order.gateway == "zarinpal"


def test_builder_chaining():
    """test: hame method ha dar yek zanjire kar mikonand."""
    order = (
        OrderBuilder()
        .add_item(PizzaMargherita("L"), qty=2)
        .add_item(Espresso(), qty=1)
        .with_coupon("WELCOME10")
        .deliver_to("Mashhad, Imam St.")
        .pay_with("idpay")
        .build()
    )

    assert len(order.items) == 2
    assert order.coupon == "WELCOME10"
    assert order.address == "Mashhad, Imam St."
    assert order.gateway == "idpay"


def test_builder_raises_error_when_no_items():
    """test: build ba sefareshe khali bayad error bede."""
    try:
        OrderBuilder().build()
        assert False, "bayad ValueError bede"
    except ValueError:
        assert True


def test_builder_fluent_api():
    """test: har method bayad self ro bargardoone."""
    builder = OrderBuilder()

    assert builder.add_item(Espresso()) is builder
    assert builder.with_coupon("TEST") is builder
    assert builder.deliver_to("Test") is builder
    assert builder.pay_with("test") is builder


if __name__ == "__main__":
    test_builder_add_item()
    test_builder_with_coupon()
    test_builder_deliver_to()
    test_builder_pay_with()
    test_builder_chaining()
    test_builder_raises_error_when_no_items()
    test_builder_fluent_api()
