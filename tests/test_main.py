"""Test module for OperationCommand and HistoryManager."""


from app.history_manager import (
    OperationCommand,
    HistoryManager,
)

def __init__(self, operation: str, a: float, b: float, result: float) -> None:
    self.operation = operation
    self.a = a
    self.b = b
    self.result = result


def test_operation_command_creation():
    """
    Test that OperationCommand is created correctly with the given parameters.
    """
    # Define test data
    operation = 'add'
    a = 5.0
    b = 10.0
    result = 15.0

    # Create an OperationCommand instance
    command = OperationCommand(operation, a, b, result)

    # Check that the attributes are set correctly
    assert command.operation == operation
    assert command.a == a
    assert command.b == b
    assert command.result == result

    # Test the __str__ method
    expected_str = f"{operation} {a} {b} = {result}"
    assert str(command) == expected_str


def test_add_to_history():
    """
    Test adding an operation to the history.
    """
    # Create an OperationCommand instance
    command = OperationCommand('subtract', 10.0, 5.0, 5.0)

    # Create a HistoryManager instance
    history_manager = HistoryManager()

    # Add the command to history and verify that it is stored correctly
    history_manager.add_to_history(command)
    assert len(history_manager.get_full_history()) == 1
    assert history_manager.get_full_history()[0] == command


def test_get_latest():
    """
    Test retrieving the latest n operations from history.
    """
    # Create OperationCommand instances
    command1 = OperationCommand('add', 5.0, 5.0, 10.0)
    command2 = OperationCommand('multiply', 4.0, 5.0, 20.0)

    # Create a HistoryManager instance
    history_manager = HistoryManager()

    # Add two commands to history
    history_manager.add_to_history(command1)
    history_manager.add_to_history(command2)

    # Retrieve the latest operation
    latest_operation = history_manager.get_latest(1)
    assert len(latest_operation) == 1
    assert latest_operation[0] == command2

    # Retrieve the latest 2 operations
    latest_two_operations = history_manager.get_latest(2)
    assert len(latest_two_operations) == 2
    assert latest_two_operations == [command1, command2]



def test_clear_history():
    """
    Test clearing the history.
    """
    # Create OperationCommand instances
    command1 = OperationCommand('divide', 10.0, 2.0, 5.0)
    command2 = OperationCommand('mod', 10.0, 3.0, 1.0)

    # Create a HistoryManager instance
    history_manager = HistoryManager()

    # Add two commands to history
    history_manager.add_to_history(command1)
    history_manager.add_to_history(command2)

    # Verify that history has two commands before clearing
    assert len(history_manager.get_full_history()) == 2
    assert command1 in history_manager.get_full_history()
    assert command2 in history_manager.get_full_history()

    # Clear the history
    history_manager.clear_history()

    # Assert that the history is now empty
    assert len(history_manager.get_full_history()) == 0


def test_undo_last():
    """
    Test undoing the last operation in history.
    """
    # Create OperationCommand instances
    command1 = OperationCommand('power', 2.0, 3.0, 8.0)
    command2 = OperationCommand('subtract', 10.0, 5.0, 5.0)

    # Create a HistoryManager instance
    history_manager = HistoryManager()

    # Add two commands to history
    history_manager.add_to_history(command1)
    history_manager.add_to_history(command2)

    # Undo the last operation and verify the result
    last_operation = history_manager.undo_last()
    assert last_operation == command2
    assert len(history_manager.get_full_history()) == 1

    # Undo the next operation
    last_operation = history_manager.undo_last()
    assert last_operation == command1
    assert len(history_manager.get_full_history()) == 0

    # Ensure that undoing when the history is empty returns None
    last_operation = history_manager.undo_last()
    assert last_operation is None
