from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for characters"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive=True):
        """Constructor of Character class"""
        if not isinstance(first_name, str):
            raise TypeError("first_name should be a string")
        self.first_name = first_name
        self.is_alive = is_alive
    
    def __str__(self):
        """Return a string representation for end-users."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return an unambiguous string representation for developers."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """Method to kill a character"""
        self.is_alive = False


class Stark(Character):
    """Class for the Starks familly"""
    def __init__(self, first_name, is_alive=True):
        """Constructor of Stark class"""
        super().__init__(first_name, is_alive)
