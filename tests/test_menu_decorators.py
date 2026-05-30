"""Tests for menu decorators (ExtraCheese, ExtraMushroom, Milk, Sugar, WithoutOnion)."""

import sys
import os

sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
)

from taamekhoob.menu.concrete_items import PizzaMargherita, Espresso
from taamekhoob.menu.decorators import (
    ExtraCheese,
    ExtraMushroom,
    Milk,
    Sugar,
    WithoutOnion,
)


def test_extra_cheese():
    """ExtraCheese bayad 15000 be gheymat ezafe kone."""

    pizza = PizzaMargherita("M")
    gheymat_asli = pizza.cost()

    pizza_ba_paneer = ExtraCheese(pizza)

    assert pizza_ba_paneer.cost() == gheymat_asli + 15000
    assert "+ Extra Cheese" in pizza_ba_paneer.description()


def test_extra_mushroom():
    """ExtraMushroom bayad 12000 be gheymat ezafe kone."""

    pizza = PizzaMargherita("M")
    gheymat_asli = pizza.cost()

    pizza_ba_gharch = ExtraMushroom(pizza)

    assert pizza_ba_gharch.cost() == gheymat_asli + 12000
    assert "+ Extra Mushroom" in pizza_ba_gharch.description()


def test_milk():
    """Milk bayad 10000 be gheymat ezafe kone."""

    coffee = Espresso()
    gheymat_asli = coffee.cost()

    coffee_ba_shir = Milk(coffee)

    assert coffee_ba_shir.cost() == gheymat_asli + 10000
    assert "+ Milk" in coffee_ba_shir.description()


def test_sugar():
    """Sugar bayad 5000 be gheymat ezafe kone."""

    coffee = Espresso()
    gheymat_asli = coffee.cost()

    coffee_ba_shekar = Sugar(coffee)

    assert coffee_ba_shekar.cost() == gheymat_asli + 5000
    assert "+ Sugar" in coffee_ba_shekar.description()


def test_without_onion():
    """WithoutOnion bayad gheymat ro taghir nade."""

    pizza = PizzaMargherita("M")
    gheymat_asli = pizza.cost()

    pizza_bi_piyaz = WithoutOnion(pizza)

    assert pizza_bi_piyaz.cost() == gheymat_asli
    assert "(no onion)" in pizza_bi_piyaz.description()


def test_double_cheese():
    """mishe do bar paneer ezafe kard."""

    pizza = PizzaMargherita("M")
    gheymat_asli = pizza.cost()

    pizza_do_paneer = ExtraCheese(ExtraCheese(pizza))

    assert pizza_do_paneer.cost() == gheymat_asli + 30000

    assert pizza_do_paneer.description().count("+ Extra Cheese") == 2


def test_chand_ta_decorator():
    """chand ta decorator ba ham kar mikonand."""

    pizza = PizzaMargherita("L")
    gheymat_asli = pizza.cost()

    pizza = ExtraCheese(pizza)
    pizza = ExtraMushroom(pizza)
    pizza = WithoutOnion(pizza)

    expected = gheymat_asli + 15000 + 12000
    assert pizza.cost() == expected
    assert "+ Extra Cheese" in pizza.description()
    assert "+ Extra Mushroom" in pizza.description()
    assert "(no onion)" in pizza.description()


def test_ahamiate_order():
    """neshonon mide tartib decorator ha to tozihat asar dare"""

    pizza = PizzaMargherita("M")

    pizza1 = ExtraMushroom(ExtraCheese(pizza))
    pizza2 = ExtraCheese(ExtraMushroom(pizza))

    assert pizza1.cost() == pizza2.cost()

    print("\n importance of order test:")
    print(f"  mushroom after cheese: {pizza1.description()}")
    print(f"  cheese after mushroom: {pizza2.description()}")

    assert pizza1.description() != pizza2.description()


if __name__ == "__main__":
    test_extra_cheese()
    test_extra_mushroom()
    test_milk()
    test_sugar()
    test_without_onion()
    test_double_cheese()
    test_chand_ta_decorator()
    test_ahamiate_order()
