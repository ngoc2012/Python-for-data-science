import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """ Return a list of BMI values. """
    try:
        h = np.array(height)
        w = np.array(weight)
    except Exception as e:
        raise TypeError("height and weight must be a list of int or float")
    assert h.size == w.size, "height and weight must have the same length"
    assert h.dtype == np.float64 or h.dtype == np.int64, "height must be int or float"
    assert w.dtype == np.float64 or w.dtype == np.int64, "weight must be int or float"
    assert np.all(h > 0) and np.all(w > 0), "height and weight must be positive"
    return (w / h ** 2).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """ Return a list of True if the BMI is greater than the limit, False otherwise. """
    assert isinstance(limit, int), "limit must be int"
    try:
        b = np.array(bmi)
    except Exception as e:
        raise TypeError("bmi must be a list of int or float")
    assert b.dtype == np.float64 or b.dtype == np.int64, "height must be int or float"
    assert np.all(b > 0), "bmi must be positive"
    return (bmi > limit).tolist()
