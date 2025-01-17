def callLimit(limit: int):
    """Outer Function: This function takes an argument (limit) \
and returns the actual decorator (callLimiter)."""
    if not isinstance(limit, int):
        raise TypeError("limit must be an integer")
    count = 0
    def callLimiter(function):
        """Decorator Function: This function takes the target function \
(function) as its input. It wraps the target function \
with additional behavior (in this case, limiting the number of calls)."""
        def limit_function(*args: any, **kwds: any):
            """Wrapper Function: This function performs the desired modification or enhancement. \
It keeps track of how many times the target function is called \
and raises an error if the limit is exceeded. \
The actual function is called only if the conditions are met."""
            nonlocal count
            count += 1
            if count > limit:
                print(f"Error: {function} call too many times")
                return None
            return function(*args, **kwds)
        return limit_function
    return callLimiter
