from typing import List, Union


# Command pattern for executing operations
class OperationCommand:
    """
    Represents a record of an operation performed, used for history tracking.
    """

    def __init__(self, operation: str, a: float, b: float, result: float) -> None:
        self.operation = operation  # The operation performed (e.g., 'add')
        self.a = a                  # The first operand
        self.b = b                  # The second operand
        self.result = result        # The result of the operation

    def __str__(self) -> str:
        return f"{self.operation} {self.a} {self.b} = {self.result}"


class HistoryManager:
    """
    Manages the history of executed operations.

    This class allows adding to, retrieving, and undoing from a history of operations.
    It stores a list of `OperationCommand` objects representing each calculation.

    Attributes:
    _history (List[OperationCommand]): List of operations executed.
    """

    def __init__(self) -> None:
        """Initializes the history manager with an empty history list."""
        self._history: List[OperationCommand] = []

    def add_to_history(self, operation: 'OperationCommand') -> None:

        self._history.append(operation)

    def get_latest(self, n: int = 1) -> List['OperationCommand']:
      
        return self._history[-n:]

    def clear_history(self) -> None:
        """Clear the entire history."""
        self._history.clear()

    def get_full_history(self) -> List['OperationCommand']:

        return self._history

    def undo_last(self) -> Union['OperationCommand', None]:
      
        if self._history:
            return self._history.pop()
        return None