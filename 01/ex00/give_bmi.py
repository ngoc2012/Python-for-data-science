def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """ Return a list of BMI values. """
    assert len(height) == len(weight), "height and weight must have the same length"
    assert len([h for h in height if h <= 0]) == 0, "height must be positive"
    assert len([w for w in weight if w <= 0]) == 0, "weight must be positive"
    assert all(isinstance(h, (int, float)) for h in height), "height must be int or float"
    assert all(isinstance(w, (int, float)) for w in weight), "weight must be int or float"
    return [weight[i] / height[i] ** 2 for i in range(len(height))]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """ Return a list of True if the BMI is greater than the limit, False otherwise. """
    assert all(isinstance(b, (int, float)) for b in bmi), "bmi must be int or float"
    return [bmi[i] > limit for i in range(len(bmi))]
