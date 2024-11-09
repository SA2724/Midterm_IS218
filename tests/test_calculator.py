"""Test module for Calculator operations and history management."""

from app.calculator import Calculator
from app.calculation import Addition, Subtraction, Multiplication
from app.history_manager import HistoryManager, OperationCommand
from unittest.mock import patch, mock_open, MagicMock


from main import CommandProcessor


def test_perform_operation():
    """
    Test that Calculator performs an operation and stores it in the history.
    """
    # Use a real Addition instance
    operation = Addition.create(5, 10)

    # Create an instance of the Calculator
    calculator = Calculator()

    # Perform the operation and assert the result
    result = calculator.perform_operation(operation)
    assert result == 15

    # Check that the operation was added to the history
    history = calculator.get_history()
    assert len(history) == 1
    assert isinstance(history[0], OperationCommand)
    assert history[0].operation == 'add'
    assert history[0].a == 5
    assert history[0].b == 10
    assert history[0].result == 15


def test_get_history():
    """
    Test that Calculator retrieves the full history of operations.
    """
    # Use real instances
    operation1 = Addition.create(5, 5)
    operation2 = Multiplication.create(4, 5)

    # Create an instance of the Calculator
    calculator = Calculator()

    # Perform two operations
    calculator.perform_operation(operation1)
    calculator.perform_operation(operation2)

    # Retrieve the full history
    history = calculator.get_history()
    assert len(history) == 2
    assert isinstance(history[0], OperationCommand)
    assert history[0].operation == 'add'
    assert history[1].operation == 'multiply'
