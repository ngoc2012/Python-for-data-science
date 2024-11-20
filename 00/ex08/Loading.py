def ft_tqdm(lst: range) -> None:
    """Display a progress bar"""
    width = 50
    for i in lst:
        yield i
        bar = int((i + 1) * width / len(lst)) * "\u2588"
        print(f"\r{int(i * 100 / len(lst)):3d}%|{bar}| {i}/{len(lst)}", end="", flush=True)
