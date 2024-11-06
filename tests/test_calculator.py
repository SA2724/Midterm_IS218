"""Test module for Calculator operations and history management."""

from app.calculator import Calculator
from app.calculation import Addition, Division, Power, Subtraction, Multiplication, Modulus
from app.history_manager import OperationCommand

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


def test_undo():
    """
    Test that Calculator can undo the last operation.
    """
    # Use real instances
    operation1 = Subtraction.create(15, 5)
    operation2 = Multiplication.create(4, 5)

    # Create an instance of the Calculator
    calculator = Calculator()

    # Perform two operations
    calculator.perform_operation(operation1)
    calculator.perform_operation(operation2)

    # Undo the last operation and check that the correct operation was undone
    last_operation = calculator.undo()
    assert last_operation.operation == 'multiply'

    # Check that the history now contains only the first operation
    history = calculator.get_history()
    assert len(history) == 1
    assert history[0].operation == 'subtract'

    # Undo the first operation
    last_operation = calculator.undo()
    assert last_operation.operation == 'subtract'

    # Check that the history is now empty
    assert len(calculator.get_history()) == 0

    # Undo when history is empty
    last_operation = calculator.undo()
    assert last_operation is None


def test_clear_history():
    """
    Test that Calculator can clear the history.
    """
    # Use real instances
    operation1 = Addition.create(5, 5)
    operation2 = Multiplication.create(4, 5)

    # Create an instance of the Calculator
    calculator = Calculator()

    # Perform two operations
    calculator.perform_operation(operation1)
    calculator.perform_operation(operation2)

    # Clear the history
    calculator.clear_history()

    # Check that the history is empty
    history = calculator.get_history()
    assert len(history) == 0
