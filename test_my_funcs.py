import pytest
from my_funcs import sum_of_index, Product, find_binary

@pytest.mark.parametrize('numbers, expected_result', [([2, 3, 5, 9, 3], 12), ([1, 2, 3, 4, 5], 6)])
def test_sum_of_index(numbers, expected_result):
    assert sum_of_index(numbers) == expected_result

@pytest.mark.parametrize('numbers, expected_result', [([2, 3, 4, 5, 6], [12, 15, 16]), ([2, 3, 5, 6], [12, 15])])
def test_Product(numbers, expected_result):
    assert Product(numbers) == expected_result

@pytest.mark.parametrize('num10, expected_result', [(45, '101101'), (3, '11'), (2, '10')])
def test_find_binary(num10, expected_result):
    assert find_binary(num10) == expected_result
