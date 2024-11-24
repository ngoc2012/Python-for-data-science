import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """ Return a list of BMI values. """
    assert isinstance(height, list), "height must be a list"
    assert isinstance(weight, list), "weight must be a list"
    h = np.array(height)
    w = np.array(weight)
    assert h.size == w.size, "height and weight must have the same length"
    assert h.dtype == np.float64 or h.dtype == np.int64, "height must be int or float"
    assert w.dtype == np.float64 or w.dtype == np.int64, "weight must be int or float"
    assert np.all(h > 0) and np.all(w > 0), "height and weight must be positive"
    return (w / h ** 2).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """ Return a list of True if the BMI is greater than the limit, False otherwise. """
    assert isinstance(bmi, list), "bmi must be a list"
    assert all(isinstance(b, (int, float)) for b in bmi), "bmi must be int or float"
    assert isinstance(limit, int), "limit must be int"
    assert all(b > 0 for b in bmi), "bmi must be positive"
    return [bmi[i] > limit for i in range(len(bmi))]
