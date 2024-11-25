import numpy as np


def isNumber(n: int | float) -> bool:
    """ Return True if n is int or float. """
    return isinstance(n, int) or isinstance(n, float)


def slice_me(family: list, start: int, end: int) -> list:
    """ Return a list of BMI values. """
    if not isinstance(family, list):
        raise TypeError("family must be a list")
    f = np.array(family)
    print(f.shape)
    if any(not isNumber(i) for i in height):
        raise TypeError("height must be a list of int or float")
    if any(not isNumber(i) for i in weight):
        raise TypeError("weight must be a list of int or float")
    h = np.array(height)
    w = np.array(weight)
    if h.size != w.size:
        raise TypeError("height and weight must have the same length")
    if np.any(h <= 0) or np.any(w <= 0):
        raise ValueError("height and weight must be positive")
    if np.any(h <= 0):
        raise ValueError("height must be positive")
    if np.any(w <= 0):
        raise ValueError("weight must be positive")
    return (w / h ** 2).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """ Return a list of True if the BMI is greater than the limit."""
    if not isinstance(limit, int):
        raise TypeError("limit must be int")
    if not isinstance(bmi, list):
        raise TypeError("bmi must be a list")
    if any(not isNumber(i) for i in bmi):
        raise TypeError("bmi must be a list of int or float")
    b = np.array(bmi)
    if np.any(b <= 0):
        raise ValueError("bmi must be positive")
    return (b > limit).tolist()
