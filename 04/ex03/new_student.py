import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random student ID"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student class"""
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        """__post_init__ runs immediately after \
the generated __init__ method"""
        self.login = self.name[0].capitalize() + self.surname.lower()
