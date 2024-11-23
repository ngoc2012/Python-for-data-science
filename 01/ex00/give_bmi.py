import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    #your code here
    assert len(height) == len(weight), "height and weight must have the same length"
    return [weight[i] / height[i] ** 2 for i in range(len(height))]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [bmi[i] > limit for i in range(len(bmi))]
    #your code here #your code here
