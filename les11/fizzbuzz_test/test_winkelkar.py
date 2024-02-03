import pytest
from .oefening_winkelkar import Checkout,CannotAddItemWithoutPriceError

def test_can_create_instance_of_checkout():
    Checkout()

@pytest.fixture()
def checkout():
    checkout_instance=checkout()
    return checkout_instance

def test_can_add_item_price():
    checkout = checkout()
    checkout.add_item_price('a',1)

def test_can_add_item_a():
    checkout= checkout()
    checkout.add_item_price('a',1)
    checkout.add_item('a')

def test_can_calculate_total():
    checkout=checkout()
    checkout.calculate_total()

def test_can_add_mult_items_and_get_correct_total():
    checkout=checkout()
    checkout.add_item_price('a',1)
    checkout.add_item_price('b',2)
    checkout.add_item('a')
    checkout.add_item('a')
    checkout.add_item('a')
    checkout.add_item('b')
    checkout.add_item('b')
    assert checkout.calculate_total == 7

def test_can_add_discount_rule():
    checkout=checkout()
    checkout.add_discount_rule('a',4,3)

#@pytest.mark.skip
def test_can_add_discount_rule_to_total():
    checkout=checkout()
    checkout.add_item_price('a',1)
    checkout.add_item_price('b',2)
    checkout.add_discount_rule('a',4,3)
    checkout.add_item('a')
    checkout.add_item('a')
    checkout.add_item('a')
    checkout.add_item('a')
    checkout.add_item('b')
    checkout.add_item('b')
    assert checkout.calculate_total == 5

def test_raise_cannot_add_item_without_price_error():
    with pytest.raises(CannotAddItemWithoutPriceError):
        checkout = checkout()
        checkout.add_item('a')