from abc import ABC, abstractmethod
from app.operations import addition, power, subtraction, multiplication, modulus, division, Number

class Calculation(ABC):
    """
    Abstract base class representing a mathematical calculation.
    
    This class defines the structure for any arithmetic operation, requiring subclasses
    to implement the `compute`, `__str__`, and `__repr__` methods. 

    Attributes:
    a (Number): The first operand (can be int or float).
    b (Number): The second operand (can be int or float).
    """

    def __init__(self, a: Number, b: Number) -> None:
        """
        Initialize the operands for the calculation.

        Args:
        a (Number): First operand.
        b (Number): Second operand.

        Raises:
        TypeError: If 'a' or 'b' are not of type int or float.
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both a and b must be numbers (int or float)")
        self.a = a
        self.b = b

    @classmethod
    def create(cls, a: Number, b: Number) -> 'Calculation':
        """
        Factory method to create a new Calculation instance.

        Args:
        a (Number): First operand.
        b (Number): Second operand.

        Returns:
        Calculation: A new instance of the calculation.
        """
        return cls(a, b)

    @abstractmethod
    def compute(self) -> Number:
        """
        Abstract method to compute the result of the calculation.
        
        Must be implemented by any subclass.

        Returns:
        Number: The result of the calculation.
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        Abstract method to return a user-friendly string representation.

        Returns:
        str: The formatted string representation of the operation.
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """
        Abstract method to return a detailed representation for debugging.

        Returns:
        str: A detailed representation of the operation.
        """
        pass

class Addition(Calculation):
    """
    Represents an addition operation.
    
    Inherits from the Calculation base class and implements the `compute`, `__str__`, and `__repr__` methods.
    """
    
    def compute(self) -> Number:
        return addition(self.a, self.b)

    def __str__(self) -> str:
        return f"Addition: {self.a} + {self.b} = {self.compute()}"

    def __repr__(self) -> str:
        return f"Addition(a={self.a}, b={self.b}, result={self.compute()})"
    
    @classmethod
    def create(cls, a: Number, b: Number) -> 'Addition':
        return cls(a, b)

    @property
    def operation(self) -> str:
        return 'add'


class Subtraction(Calculation):
    """
    Represents a subtraction operation.
    
    Inherits from the Calculation base class and implements the `compute`, `__str__`, and `__repr__` methods.
    """
    
    def compute(self) -> Number:
        return subtraction(self.a, self.b)

    def __str__(self) -> str:
        return f"Subtraction: {self.a} - {self.b} = {self.compute()}"

    def __repr__(self) -> str:
        return f"Subtraction(a={self.a}, b={self.b}, result={self.compute()})"
    
    @classmethod
    def create(cls, a: Number, b: Number) -> 'Subtraction':
        return cls(a, b)

    @property
    def operation(self) -> str:
        return 'subtract'

class Multiplication(Calculation):
    """
    Represents a multiplication operation.
    
    Inherits from the Calculation base class and implements the `compute`, `__str__`, and `__repr__` methods.
    """
    
    def compute(self) -> Number:
        return multiplication(self.a, self.b)

    def __str__(self) -> str:
        return f"Multiplication: {self.a} * {self.b} = {self.compute()}"

    def __repr__(self) -> str:
        return f"Multiplication(a={self.a}, b={self.b}, result={self.compute()})"
    
    @classmethod
    def create(cls, a: Number, b: Number) -> 'Multiplication':
        return cls(a, b)
    
    @property
    def operation(self) -> str:
        return 'multiply'

class Division(Calculation):
    """
    Represents a division operation.
    
    Inherits from the Calculation base class and implements the `compute`, `__str__`, and `__repr__` methods.
    """
    
    def compute(self) -> Number:
        if self.b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return division(self.a, self.b)
    
    @classmethod
    def create(cls, a: Number, b: Number) -> 'Division':
        """
        Factory method to create a new Division instance.

        Args:
            a (Number): The dividend.
            b (Number): The divisor.

        Returns:
            Division: A new instance of the Division class.
        """
        return cls(a, b)

    def __str__(self) -> str:
        result = self.compute()
        # If the result is a whole number, format it as an integer; otherwise, keep it as a float.
        formatted_result = int(result) if result.is_integer() else result
        return f"Division: {self.a} / {self.b} = {formatted_result}"

    def __repr__(self) -> str:
        result = self.compute()
        formatted_result = int(result) if result.is_integer() else result
        return f"Division(a={self.a}, b={self.b}, result={formatted_result})"

    @property
    def operation(self) -> str:
        return 'divide'

class Power(Calculation):
    """
    Reprsents the power function 
    
    Inherits from the Calculation base class and implements the `compute`, `__str__`, and `__repr__` methods. 
    """
    def compute(self) -> Number:
        return power(self.a, self.b)

    @classmethod
    def create(cls, a: Number, b: Number) -> 'Power':
        """
        Factory method to create a new Power instance.

        Args:
            a (Number): The base number.
            b (Number): The exponent.

        Returns:
            Power: A new instance of the Power calculation.
        """
        return cls(a, b)
    def __str__(self) -> str:
        return f"Power: {self.a} ** {self.b} = {self.compute()}"

    def __repr__(self) -> str:
        return f"Power(a={self.a}, b={self.b}, result={self.compute()})"

    @property
    def operation(self) -> str:
        return 'power'

class Modulus(Calculation):
    """
    Represents a modulus operation.
    
    Inherits from the Calculation base class and implements the `compute`, `__str__`, `__repr__` methods.
    """
    @classmethod
    def create(cls, a: Number, b: Number) -> 'Modulus':
        """
        Class method to create a new Modulus instance.

        Args:
            a (Number): The first operand.
            b (Number): The second operand.

        Returns:
            Modulus: A new instance of Modulus with the given operands.
        """
        return cls(a, b)
    
    def compute(self) -> Number:
        """
        Computes the modulus of the two operands.
        
        Raises:
            ZeroDivisionError: If the second operand is zero.
        
        Returns:
            Number: The result of the modulus operation.
        """
        if self.b == 0:
            raise ZeroDivisionError("Modulus by zero is not allowed")
        return modulus(self.a, self.b)
    
    def __str__(self) -> str:
        """
        Returns a user-friendly string representation of the modulus operation.
        
        Returns:
            str: Formatted string showing the operation and result.
        """
        return f"Modulus: {self.a} % {self.b} = {self.compute()}"
    
    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the modulus operation for debugging.
        
        Returns:
            str: Detailed representation including operands and result.
        """
        return f"Modulus(a={self.a}, b={self.b}, result={self.compute()})"

    @property
    def operation(self) -> str:
        return 'mod'
