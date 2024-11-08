# tests/test_calculation.py
"""
Unit test for the Calculator's ability to perform operations
"""
from unittest.mock import Mock

from app.calculator import Calculator
from app.history_manager import OperationCommand

def test_perform_operation_add():
    """
    Test that Calculator performs an operation and stores it in the history.
    """
    # Create a mock Calculation object
    mock_operation = Mock()
    mock_operation.compute.return_value = 15
    mock_operation.a = 5
    mock_operation.b = 10
    mock_operation.operation = 'add'

    # Create an instance of the Calculator
    calculator = Calculator()

    # Perform the operation and assert the result
    result = calculator.perform_operation(mock_operation)
    assert result == 15
    mock_operation.compute.assert_called_once()

    # Check that the operation was added to the history
    history = calculator.get_history()
    assert len(history) == 1
    assert isinstance(history[0], OperationCommand)
    assert history[0].operation == 'add'
    assert history[0].a == 5
    assert history[0].b == 10
    assert history[0].result == 15

def test_perform_operation_subtract():
    """
    Test that Calculator performs an operation and stores it in the history.
    """
    # Create a mock Calculation object
    mock_operation = Mock()
    mock_operation.compute.return_value = -5
    mock_operation.a = 5
    mock_operation.b = 10
    mock_operation.operation = 'subtract'

    # Create an instance of the Calculator
    calculator = Calculator()

    # Perform the operation and assert the result
    result = calculator.perform_operation(mock_operation)
    assert result == -5
    mock_operation.compute.assert_called_once()

    # Check that the operation was added to the history
    history = calculator.get_history()
    assert len(history) == 1
    assert isinstance(history[0], OperationCommand)
    assert history[0].operation == 'subtract'
    assert history[0].a == 5
    assert history[0].b == 10
    assert history[0].result == -5

def test_perform_operation_multiply():
    """
    Test that Calculator performs an operation and stores it in the history.
    """
    # Create a mock Calculation object
    mock_operation = Mock()
    mock_operation.compute.return_value = 50
    mock_operation.a = 5
    mock_operation.b = 10
    mock_operation.operation = 'multiply'

    # Create an instance of the Calculator
    calculator = Calculator()

    # Perform the operation and assert the result
    result = calculator.perform_operation(mock_operation)
    assert result == 50
    mock_operation.compute.assert_called_once()

    # Check that the operation was added to the history
    history = calculator.get_history()
    assert len(history) == 1
    assert isinstance(history[0], OperationCommand)
    assert history[0].operation == 'multiply'
    assert history[0].a == 5
    assert history[0].b == 10
    assert history[0].result == 50
