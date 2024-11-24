import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """ Return a list of BMI values. """
    assert isinstance(height, list), "height must be a list"
    assert isinstance(weight, list), "weight must be a list"
    assert len(height) == len(weight), "height and weight must have the same length"
    assert all(isinstance(h, (int, float)) for h in height), "height must be int or float"
    assert all(isinstance(w, (int, float)) for w in weight), "weight must be int or float"
    assert all(h > 0 for h in height), "height must be positive"
    assert all(w > 0 for w in weight), "weight must be positive"
    h = np.array(height)
    w = np.array(weight)
    return list(w / h ** 2)
    #return [weight[i] / height[i] ** 2 for i in range(len(height))]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """ Return a list of True if the BMI is greater than the limit, False otherwise. """
    assert isinstance(bmi, list), "bmi must be a list"
    assert all(isinstance(b, (int, float)) for b in bmi), "bmi must be int or float"
    assert isinstance(limit, int), "limit must be int"
    assert all(b > 0 for b in bmi), "bmi must be positive"
    return [bmi[i] > limit for i in range(len(bmi))]
