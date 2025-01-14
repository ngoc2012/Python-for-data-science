from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King family."""
    def __init__(self, first_name: str, is_alive: bool=True):
        """Constructor of King class"""
        if not isinstance(first_name, str):
            raise TypeError("first_name should be a string")
        if not isinstance(is_alive, bool):
            raise ValueError("is_alive must be a boolean.")
        Lannister.__init__(self, first_name, is_alive)
        Baratheon.__init__(self, first_name, is_alive)

    def set_eyes(self, color: str):
        """Set the color of the eyes"""
        if not isinstance(color, str):
            raise TypeError("color should be a string")
        self.eyes = color

    def set_hairs(self, color: str):
        """Set the color of the hairs"""
        if not isinstance(color, str):
            raise TypeError("color should be a string")
        self.hairs = color

    def get_eyes(self):
        """Get the color of the eyes"""
        return self.eyes

    def get_hairs(self):
        """Get the color of the hairs"""
        return self.hairs
