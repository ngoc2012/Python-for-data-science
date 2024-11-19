from typing import Callable, Iterable


def ft_filter(f: Callable, it: Iterable) -> Iterable:
    """Filter function return a new list with elements that pass\
 the test implemented by the function f"""
    return [x for x in it if f(x)]
