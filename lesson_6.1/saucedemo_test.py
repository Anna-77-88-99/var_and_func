import pytest
from saucedemo import SwagLabs

sl = SwagLabs()

@pytest.mark.parametrize('price', [('Total: $58.29')])
def test_shop(price):
    price_value = sl.price_value
    assert price == price_value