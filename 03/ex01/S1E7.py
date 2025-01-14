from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name: str, is_alive:bool = True):
        """Constructor of Baratheon class"""
        if not isinstance(first_name, str):
            raise TypeError("first_name should be a string")
        if not isinstance(is_alive, bool):
            raise ValueError("is_alive must be a boolean.")
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name: str, is_alive:bool = True):
        """Constructor of Lannister class"""
        if not isinstance(first_name, str):
            raise TypeError("first_name should be a string")
        if not isinstance(is_alive, bool):
            raise ValueError("is_alive must be a boolean.")
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Create a Lannister character"""
        return cls(first_name, is_alive)
