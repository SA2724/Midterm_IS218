import csv
import os
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
    
    def undo_last(self):
        """Undoes the last executed command, if any exist in history."""
        last_command = self.history_manager.pop_last()
        if last_command:
            last_command.undo()
        print("Last operation undone.")

    def undo(self) -> None:
        """
        Undo the operation.

        For a stateless calculator, undoing can simply involve notifying that the operation
        has been removed from history. No state changes are required.
        """
        print(f"Undoing operation: {self}")
    def to_dict(self) -> dict:
        """Convert the command to a dictionary for easy CSV conversion."""
        return {
            "operation": self.operation,
            "a": self.a,
            "b": self.b,
            "result": self.result
        }

class HistoryManager:
    """
    Manages the history of executed operations using lists.

    This class allows adding to, retrieving, saving, loading, clearing, and undoing history records.
    Calculation history is stored in a CSV file for persistence across sessions.
    """

    def __init__(self, history_file: str = "history.csv") -> None:
        """Initializes the history manager with a specified history file."""
        self.history_file = history_file
        self._history: List[OperationCommand] = []  # Stores the history as a list of OperationCommand
        # Load existing history if available
        self.load_history()

    def add_to_history(self, operation: 'OperationCommand') -> None:
        """Add an operation to the history and save it to CSV."""
        self._history.append(operation)
        self.save_history()

    def get_latest(self, n: int = 1) -> List[OperationCommand]:
        """Retrieve the latest n operations."""
        return self._history[-n:]

    def clear_history(self) -> None:
        """Clear the entire history and remove the CSV file."""
        self._history = []
        self.save_history()

    def get_full_history(self) -> List[OperationCommand]:
        """Retrieve the entire history."""
        return self._history

    def undo_last(self) -> Union[OperationCommand, None]:
        """Remove the last operation from history and return it."""
        if self._history:
            last_entry = self._history.pop()
            self.save_history()
            return last_entry
        return None

    def save_history(self) -> None:
        """Save the current history to the CSV file."""
        with open(self.history_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["operation", "a", "b", "result"])
            writer.writeheader()
            for command in self._history:
                writer.writerow(command.to_dict())

    def pop_last(self) -> Union[OperationCommand, None]:
        """Remove and return the last operation from history."""
        if self._history:
            last_command = self._history.pop()
            self.save_history()
            return last_command
        return None

    def load_history(self) -> None:
        """Load history from the CSV file if it exists."""
        if os.path.exists(self.history_file):
            with open(self.history_file, mode='r') as file:
                reader = csv.DictReader(file)
                self._history = [
                    OperationCommand(
                        operation=row["operation"],
                        a=float(row["a"]),
                        b=float(row["b"]),
                        result=float(row["result"])
                    ) for row in reader
                ]
