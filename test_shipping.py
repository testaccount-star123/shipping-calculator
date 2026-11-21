import pytest
from shipping import shipping_cost


def test_one_kg_standard():
    assert shipping_cost(1) == 4.0


def test_three_kg_standard():
    assert shipping_cost(3) == 7.0


def test_one_kg_express():
    assert shipping_cost(1, express=True) == 7.2


def test_rejects_zero_weight():
    with pytest.raises(ValueError):
        shipping_cost(0)


def test_two_kg_express():
    assert shipping_cost(2, express=True) == 9.9
