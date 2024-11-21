def ft_tqdm(lst: range) -> None:
    """Display a progress bar"""
    width = 43
    for i in lst:
        yield i
        current = int((i + 1) * width / len(lst))
        bar = current * "\u2588" + (width - current) * " "
        print(f"\r{int((i + 1) * 100 / len(lst)):3d}%|{bar}| {i + 1}/{len(lst)}", end="", flush=True)
