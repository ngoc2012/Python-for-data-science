import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """ Return a list of BMI values. """
    if not isinstance(family, list):
        raise TypeError("family must be a list")
    f = np.array(family)
    print(f"My shape is : {f.shape}")
    if start < f.shape[0] and end > f.shape[0]:
    return f
