def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        nonlocal count, x
        def limit_function(*args: Any, **kwds: Any):
        #your code here

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
