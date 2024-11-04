from typing import List, Union

from app.calculation import Calculation
from app.operations import Number

# Command pattern for executing operations
class OperationCommand:
    def __init__(self, operation: Calculation) -> None:
        self.operation = operation

    def execute(self) -> Number:
        return self.operation.compute()

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