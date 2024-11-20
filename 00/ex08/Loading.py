def ft_tqdm(lst: range) -> None:
    """Display a progress bar"""
    for i in lst:
        yield i
def ft_filter(f: Callable, it: Iterable) -> Iterable:
    """Filter function return a new list with elements that pass\
 the test implemented by the function f"""
    return [x for x in it if f(x)]
