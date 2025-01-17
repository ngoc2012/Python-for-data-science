import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random student ID"""
    return "".join(random.choices(string.ascii_lowercase, k = 15))


@dataclass
class Student:
    #your code here
