import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float])\
        -> list[int | float]:
    """ Return a list of BMI values. """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("height, weight must be a list")
    h = np.array(height)
    w = np.array(weight)
    if h.dtype not in [np.float64, np.int64]:
        raise TypeError("height must be a list of int or float")
    if w.dtype not in [np.float64, np.int64]:
        raise TypeError("weight must be a list of int or float")
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
    b = np.array(bmi)
    if b.dtype not in [np.float64, np.int64] or len(b.shape) != 1:
        raise TypeError("bmi must be a list of int or float")
    if np.any(b <= 0):
        raise ValueError("bmi must be positive")
    return (b > limit).tolist()
