import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """ Return a list of BMI values. """
    if not isinstance(family, list):
        raise TypeError("family must be a list")
    f = np.array(family)
    rows = f.shape[0]
    if start < rows or end > rows or -end > rows:
        raise IndexError("Index out of range")
    print(f"My shape is : {f.shape}")
    return f[start:end]
