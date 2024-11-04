'''My Calculator Test with Fixtures and Parameterization'''
import pytest
from main import addition, division, multiplication, subtraction

@pytest.fixture
def add_data():
    """Fixture for addition test data"""
    return [
        (1, 1, 2),
        (2, 3, 5),
        (-1, -1, -2),
        (-1, 1, 0),
        (0, 0, 0)
    ]

@pytest.fixture
def subtract_data():
    """Fixture for subtraction test data"""
    return [
        (1, 1, 0),
        (5, 3, 2),
        (-1, -1, 0),
        (-1, 1, -2),
        (0, 0, 0)
    ]

@pytest.fixture
def multiply_data():
    """Fixture for multiplication test data"""
    return [
        (1, 2, 2),
        (3, 4, 12),
        (-1, -2, 2),
        (-1, 2, -2),
        (0, 5, 0)
    ]

@pytest.fixture
def divide_data():
    """Fixture for division test data"""
    return [
        (4, 2, 2),
        (10, 5, 2),
        (-4, -2, 2),
        (-4, 2, -2),
        (0, 1, 0)
    ]

@pytest.fixture
def divide_zero_data():
    """Fixture for division by zero test cases"""
    return [
        (10, 0),
        (-5, 0),
        (0, 0)
    ]

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (-1, -1, -2),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_addition(a, b, expected):
    """Addition Function"""
    assert addition(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 0),
    (5, 3, 2),
    (-1, -1, 0),
    (-1, 1, -2),
    (0, 0, 0)
])
def test_subtraction(a, b, expected):
    """Subtraction Function"""
    assert subtraction(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 2),
    (3, 4, 12),
    (-1, -2, 2),
    (-1, 2, -2),
    (0, 5, 0)
])
def test_multiplication(a, b, expected):
    """Multiplication Function"""
    assert multiplication(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (4, 2, 2),
    (10, 5, 2),
    (-4, -2, 2),
    (-4, 2, -2),
    (0, 1, 0)
])
def test_division(a, b, expected):
    """Division Function"""
    assert division(a, b) == expected

@pytest.mark.parametrize("a, b", [
    (10, 0),
    (-5, 0),
    (0, 0)
])
def test_division_by_zero(a, b):
    """Division by Zero Function"""
    with pytest.raises(ZeroDivisionError):
        division(a, b)
