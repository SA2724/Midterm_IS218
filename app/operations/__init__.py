from typing import Union

# Define a type alias for numbers (both int and float)

Number = Union[int, float]

# addition function 
def addition(a: Number, b: Number) -> Number:
   
    return a +  b  # Return the result of a plus b

def subtraction(a: Number, b: Number) -> Number:

    return a - b #return result of a minus b 

def multiplication(a: Number, b: Number) -> Number:
    
    return a * b  # Return the product of a and b

def division(a: Number, b: Number) -> Number:

    return a / b  # Return the result of a divided by b