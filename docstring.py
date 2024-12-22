def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract two numbers and return the result."""
    return a - b

print("###############################3###########")

class Calculator:
    """
    A simple calculator class for basic arithmetic operations.

    Methods:
        add(a, b): Returns the sum of two numbers.
        subtract(a, b): Returns the difference between two numbers.
    """
    def add(self, a, b):
        """Add two numbers and return the result."""
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers and return the result."""
        return a - b
    
print("###############################3###########")

def divide(a, b):
    """
    Divide two numbers.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of division.

    Raises:
        ZeroDivisionError: If the denominator is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    return a / b

print("###############################3###########")

def square_root(x):
    """
    Compute the square root of a number.

    Parameters
    ----------
    x : float
        The number to find the square root of.

    Returns
    -------
    float
        The square root of the number.
    """
    return x ** 0.5