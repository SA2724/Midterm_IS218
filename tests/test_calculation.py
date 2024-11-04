"""Test module for operations: Addition, Subtraction, Multiplication, Division, Power, Modulus."""

from typing import Literal
import pytest
from app.calculation import (
    Addition,
    Subtraction,
    Multiplication,
    Division,
    Power,
    Modulus
)  # Assuming your classes are in the 'calculation' module

# Parameterized test for Addition with __str__ and __repr__ checks
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 2),
        (2, 3, 5),
        (-1, -1, -2),
        (0, 0, 0)
    ]
)
def test_addition(
    a: Literal[1, 2, -1, 0],
    b: Literal[1, 3, -1, 0],
    expected: Literal[2, 5, -2, 0]
):
    """Test for addition operation."""
    operation = Addition.create(a, b)
    assert operation.compute() == expected
    assert str(operation) == f"Addition: {a} + {b} = {expected}"
    assert repr(operation) == f"Addition(a={a}, b={b}, result={expected})"

# Parameterized test for Subtraction with __str__ and __repr__ checks
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 0),
        (5, 3, 2),
        (-1, -1, 0),
        (0, 5, -5)
    ]
)
def test_subtraction(
    a: Literal[1, 5, -1, 0],
    b: Literal[1, 3, -1, 5],
    expected: Literal[0, 2, -5]
):
    """Test for subtraction operation."""
    operation = Subtraction.create(a, b)
    assert operation.compute() == expected
    assert str(operation) == f"Subtraction: {a} - {b} = {expected}"
    assert repr(operation) == f"Subtraction(a={a}, b={b}, result={expected})"

# Parameterized test for Multiplication with __str__ and __repr__ checks
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 2, 4),
        (3, 5, 15),
        (0, 5, 0),
        (-1, 1, -1)
    ]
)
def test_multiplication(
    a: Literal[2, 3, 0, -1],
    b: Literal[2, 5, 1],
    expected: Literal[4, 15, 0, -1]
):
    """Test for multiplication operation."""
    operation = Multiplication.create(a, b)
    assert operation.compute() == expected
    assert str(operation) == f"Multiplication: {a} * {b} = {expected}"
    assert repr(operation) == f"Multiplication(a={a}, b={b}, result={expected})"

# Parameterized test for Division with __str__ and __repr__ checks
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 2, 1),
        (10, 5, 2),
        (9, 3, 3),
        (7, 2, 3.5)
    ]
)
def test_division(
    a: Literal[2, 10, 9, 7],
    b: Literal[2, 5, 3],
    expected: Literal[1, 2, 3] | float
):
    """Test for division operation."""
    operation = Division.create(a, b)
    assert operation.compute() == expected
    # Format expected result if it's a whole number float
    formatted_expected = int(expected) if isinstance(expected, float) and expected.is_integer() else expected
    assert str(operation) == f"Division: {a} / {b} = {formatted_expected}"
    assert repr(operation) == f"Division(a={a}, b={b}, result={formatted_expected})"

# Test for division by zero exception
def test_division_by_zero_exception():
    """Test for division by zero exception."""
    operation = Division.create(10, 0)
    with pytest.raises(ZeroDivisionError):
        operation.compute()

# Parameterized test for Power with __str__ and __repr__ checks
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 8),
        (5, 0, 1),
        (3, 4, 81),
        (2, -2, 0.25),
        (0, 5, 0),
        (0, 0, 1)  # In Python, 0**0 is defined as 1
    ]
)
def test_power(
    a: Literal[2, 5, 3, 0],
    b: Literal[3, 0, 4, -2, 5],
    expected: Literal[8, 1, 81, 0, 1] | float
):
    """Test for power operation."""
    operation = Power.create(a, b)
    assert operation.compute() == expected
    assert str(operation) == f"Power: {a} ** {b} = {expected}"
    assert repr(operation) == f"Power(a={a}, b={b}, result={expected})"

# Parameterized test for Modulus with __str__ and __repr__ checks
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 3, 1),
        (20, 5, 0),
        (-10, 3, 2),
        (10, -3, -2),
        (0, 5, 0)
    ]
)
def test_modulus(
    a: Literal[10, 20, -10, 0],
    b: Literal[3, 5, -3],
    expected: Literal[1, 0, 2, -2]
):
    """Test for modulus operation."""
    operation = Modulus.create(a, b)
    assert operation.compute() == expected
    assert str(operation) == f"Modulus: {a} % {b} = {expected}"
    assert repr(operation) == f"Modulus(a={a}, b={b}, result={expected})"

# Test for modulus by zero exception
def test_modulus_by_zero_exception():
    """Test for modulus by zero exception."""
    operation = Modulus.create(10, 0)
    with pytest.raises(ZeroDivisionError):
        operation.compute()
