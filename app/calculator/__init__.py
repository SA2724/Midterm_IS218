from typing import List, Union
from app.calculation import Calculation
from app.history_manager import HistoryManager, OperationCommand
from app.operations import Number


class Calculator:
    def __init__(self):
        self.history_manager = HistoryManager()

    def perform_operation(self, calculation):
        result = calculation.compute()
        # Assuming 'calculation' has 'operation', 'a', and 'b' attributes
        operation_command = OperationCommand(
            operation=calculation.operation,  # e.g., 'add', 'subtract'
            a=calculation.a,
            b=calculation.b,
            result=result
        )
        self.history_manager.add_to_history(operation_command)
        return result

    def get_history(self):
        return self.history_manager.get_full_history()

    def undo_last_operation(self) -> Union[OperationCommand, None]:
        return self.history_manager.undo_last()

    def clear_history(self):
        self.history_manager.clear_history()
    # In app/calculator/__init__.py or wherever your Calculator class is defined

def perform_operation(self, calculation):
    result = calculation.compute()
    operation_command = OperationCommand(
        operation=calculation.operation,  # e.g., 'add', 'subtract'
        a=calculation.a,
        b=calculation.b,
        result=result
    )
    self.history_manager.add_to_history(operation_command)
    return result
