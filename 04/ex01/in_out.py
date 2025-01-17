def square(x: int | float) -> int | float:
    """Return the square of a number."""
    return x ** 2

def pow(x: int | float) -> int | float:
    """Return the power of a number to itself."""
    return x ** x

def outer(x: int | float, function) -> object:
    count = 0
    def inner() -> float:
        nonlocal count, x
        count += 1
        return function(x)
    return inner
