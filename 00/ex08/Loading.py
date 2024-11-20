def ft_tqdm(lst: range) -> None:
    """Display a progress bar"""
    for i in lst:
        yield i
        sys.stdout.write(f'\r{desc or ""}: |{bar}| {i + 1}/{total} [{elapsed_time:.2f}s<{remaining_time:.2f}s, {rate:.2f}it/s]')
        sys.stdout.flush()

def ft_filter(f: Callable, it: Iterable) -> Iterable:
    """Filter function return a new list with elements that pass\
 the test implemented by the function f"""
    return [x for x in it if f(x)]
