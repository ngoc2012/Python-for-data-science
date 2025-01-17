def square(x: int | float) -> int | float:
    """Return the square of a number."""
    if not isinstance(x, (int, float)):
        raise TypeError("x must be an int or a float.")
    return x ** 2

def pow(x: int | float) -> int | float:
    """Return the power of a number to itself."""
    if not isinstance(x, (int, float)):
        raise TypeError("x must be an int or a float.")
    return x ** x

def outer(x: int | float, function) -> object:
    """Return a function that applies the given function to the given number."""
    count = 0
    def inner() -> float:
        """Return the result of applying the given function to the given number."""
        nonlocal count, x
        count += 1
        x = function(x)
        return x
    return inner
