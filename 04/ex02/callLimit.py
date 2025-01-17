def callLimit(limit: int):
    """Return a decorator that limits the number of times a function can be called."""
    count = 0
    def callLimiter(function):
        """Decorator Function: This function takes the target function (function) as its input. It wraps the target function with additional behavior (in this case, limiting the number of calls)."""
        def limit_function(*args: any, **kwds: any):
            """Limit the number of times a function can be called."""
            nonlocal count
            count += 1
            if count > limit:
                raise ValueError(f"Function {function} call too many times")
            return function(*args, **kwds)
        try:
            f = limit_function
        except ValueError as e:
            print(e)
        return f
    return callLimiter
