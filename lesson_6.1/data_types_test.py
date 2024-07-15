import pytest
from data_types import DataTypes

dt = DataTypes()

@pytest.mark.parametrize('red_color',[('rgba(248, 215, 218, 1)')])
def test_zip_color_red(red_color):
  
    result = dt.zip_code_color
    assert result == red_color


@pytest.mark.parametrize('nums', [(9)])
def test_all_green_colors(nums):
    list_of_green = ['rgba(209, 231, 221, 1)'] * nums
    color_list = dt.color_list
    assert list_of_green == color_list
