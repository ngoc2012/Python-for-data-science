def ft_tqdm(lst: range) -> None:
    """Display a progress bar"""
    for i in lst:
        yield i
        bar = int((i + 1) * 100 / len(lst)) * "\u2588"
        print(f"\r{int(i * 100 / len(lst))}%|{bar}", end="", flush=True)
