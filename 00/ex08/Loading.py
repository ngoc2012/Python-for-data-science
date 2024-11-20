def ft_tqdm(lst: range) -> None:
    """Display a progress bar"""
    for i in lst:
        yield i
        bar = i / len(lst) * 100 * "#"
        print(f"\r{bar}", end="", flush=True)
