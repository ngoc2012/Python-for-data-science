import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """ Return a list of BMI values. """
    h = np.array(height)
    w = np.array(weight)
    assert h.dtype == np.float64 or h.dtype == np.int64, "height must be a list of int or float"
    assert w.dtype == np.float64 or w.dtype == np.int64, "weight must be a list of int or float"
    if h.size != w.size: raise ValueError("height and weight must have the same length")
    assert np.all(h > 0) and np.all(w > 0), "height and weight must be positive"
    if np.any(h <= 0): raise ValueError("height must be positive")
    if np.any(b <= 0): raise ValueError("weight must be positive")
    return (w / h ** 2).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """ Return a list of True if the BMI is greater than the limit, False otherwise. """
    if not isinstance(limit, int): raise TypeError("limit must be int")
    b = np.array(bmi)
    if not(b.dtype == np.float64 or b.dtype == np.int64):
        raise TypeError("bmi must be a list of int or float")
    if np.any(b <= 0): raise ValueError("bmi must be positive")
    return (b > limit).tolist()
