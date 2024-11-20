def ft_tqdm(lst: range) -> None:
    """Display a progress bar"""
    for i in lst:
        yield i
        bar = int(i * 100 / len(lst)) * "#"
        print(f"\r{bar}", end="", flush=True)
