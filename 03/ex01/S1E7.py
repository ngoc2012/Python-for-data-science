from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """Constructor of Baratheon class"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        super().__str__()

    def __repr__(self):
        super().__repr__()


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        """Constructor of Lannister class"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        super().__str__()

    def __repr__(self):
        super().__repr__()

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Create a Lannister character"""
        return cls(first_name, is_alive)
