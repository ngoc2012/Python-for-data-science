from typing import Callable, Iterable

def ft_filter(f: Callable, it: Iterable) -> Iterable:
    return [x for x in it if f(x)]
