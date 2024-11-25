import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """ Return a list of BMI values. """
    if not isinstance(family, list):
        raise TypeError("family must be a list")
    f = np.array(family)
    shape = f.shape
    rows = shape[0]
    if start < 0:
        start = rows + start
    if end < 0:
        end = rows + end
    if start >= end or end > rows:
        raise IndexError("Index out of range")
    new_shape = (end - start, shape[1])
    print(f"My shape is : {shape}")
    print(f"My new shape is : {new_shape}")
    return f[start:end].tolist()
