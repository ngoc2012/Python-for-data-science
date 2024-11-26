import numpy as np


def isNumber(n: int | float) -> bool:
    """ Return True if n is int or float. """
    return isinstance(n, (int, float))


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a 2D array."""
    if not isinstance(family, list):
        raise TypeError("family must be a list")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be integers")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("family must be a 2D array")
    for row in family:
        if not all(isNumber(x) for x in row):
            raise TypeError("family must be a 2D array of numbers")
    if len(set([len(row) for row in family])) != 1:
        raise ValueError("All sublists in family must have the same length")
    f = np.array(family)
    shape = f.shape
    if len(shape) != 2:
        raise ValueError("family must be a 2D array")
    rows = shape[0]
    if start < 0:
        start = rows + start
    if end < 0:
        end = rows + end
    if start < 0 or start >= end or end > rows:
        raise IndexError("Index out of range")
    new_shape = (end - start, shape[1])
    print(f"My shape is : {shape}")
    print(f"My new shape is : {new_shape}")
    return f[start:end].tolist()
