def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            count += 1
            if count > limit:
                raise ValueError(f"Function has been called {count} times, \
which exceeds the limit of {limit}.")
            return function(*args, **kwds)
