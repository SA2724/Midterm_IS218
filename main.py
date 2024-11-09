# app/command_processor.py

from typing import Dict, Type
from app.calculation import Addition, Subtraction, Multiplication, Division, Power, Modulus
from app.calculator import Calculator
from app.history_manager import HistoryManager, OperationCommand

# Dictionary mapping operation strings to the corresponding calculation class.
operations_map: Dict[str, Type] = {
    'add': Addition,
    'subtract': Subtraction,
    'multiply': Multiplication,
    'divide': Division,
    'power': Power,
    'mod': Modulus
}

class CommandProcessor:
    """
    Processes user commands, performs calculations, and interacts with the Calculator and HistoryManager.

    Attributes:
        calculator (Calculator): The calculator to perform operations.
        history_manager (HistoryManager): Manages the history of operations.
    """
    def __init__(self) -> None:
        """Initializes the CommandProcessor with a Calculator and HistoryManager instance."""
        self.calculator = Calculator()
        self.history_manager = HistoryManager()

    def undo_last(self):
        """Undoes the last executed command, if any exist in history."""
        last_command = self.history_manager.pop_last()
        if last_command:
            last_command.undo()
            print("Last operation undone.")
        else:
            print("No commands to undo.")
    
    def execute(self, command: str) -> None:
        """
        Executes a given command, processes the operation, records it in history, and displays the result.

        Args:
            command (str): The user's input command.
        """
        # Split the command into operation and arguments
        parts = command.split()

        # Validate input command length
        if len(parts) != 3:
            print("Invalid command format. Type 'help' for instructions.")
            return

        operation, a_str, b_str = parts

        # Convert inputs to float
        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError:
            print("Invalid numbers. Please enter valid numeric values.")
            return

        # Check if the operation is valid
        if operation not in operations_map:
            print(f"Unknown operation '{operation}'. Type 'help' for instructions.")
            return

        # Instantiate the appropriate calculation class
        calculation_class = operations_map[operation]
        calculation = calculation_class.create(a, b)

        # Perform the calculation and print the result
        try:
            result = self.calculator.perform_operation(calculation)
            print(f"Result: {result}")
            print(f"Operation: {calculation}")  # This uses the __str__ of the calculation class

            # Record the operation in history
            operation_command = OperationCommand(
                operation=operation,
                a=a,
                b=b,
                result=result
            )
            self.history_manager.add_to_history(operation_command)
        except ZeroDivisionError:
            print("Error: Division by zero.")

    def show_help(self) -> None:
        """Displays the help menu with available commands."""
        print("""
Available commands:
  add a b        - Adds a and b
  subtract a b   - Subtracts b from a
  multiply a b   - Multiplies a and b
  divide a b     - Divides a by b
  power a b      - Raises the power of a by b 
  mod a b        - Modulus a by b 
  history        - Shows the operation history
  undo           - Undoes the last operation
  clear          - Clears the operation history
  exit           - Exits the REPL
  help           - Shows this help message
""")

    def show_history(self) -> None:
        """Displays the full history of operations performed."""
        history = self.history_manager.get_full_history()
        if not history:
            print("No operations in history.")
        else:
            for index, command in enumerate(history, start=1):
                print(f"{index}: {command.operation} {command.a} {command.b} = {command.result}")

    def clear_history(self) -> None:
        """Clears the operation history."""
        self.history_manager.clear_history()
        print("History cleared.")

def main():
    processor = CommandProcessor()
    print("Welcome to the Calculator REPL. Type 'help' for instructions or 'exit' to quit.")

    while True:
        try:
            command = input(">>> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if command in ['exit', 'quit']:
            print("Goodbye!")
            break
        elif command == 'help':
            processor.show_help()
        elif command == 'history':
            processor.show_history()
        elif command == 'undo':
            processor.undo_last()
        elif command == 'clear':
            processor.clear_history()
        else:
            processor.execute(command)

if __name__ == '__main__':
    main()
