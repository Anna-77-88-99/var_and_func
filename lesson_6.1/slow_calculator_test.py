import pytest
from slow_calculator import Calculator

calc = Calculator()

@pytest.mark.parametrize('calc_value', [('15')])
def test_calculator(calc_value):
    result_value = calc.resalt_value
    assert result_value == calc_value