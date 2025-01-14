from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for characters"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive:bool = True):
        """Constructor of Character class"""
        if not isinstance(first_name, str):
            raise TypeError("first_name should be a string")
        if not isinstance(is_alive, bool):
            raise TypeError("is_alive must be a boolean.")
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Method to kill a character"""
        self.is_alive = False


class Stark(Character):
    """Class for the Starks familly"""
    def __init__(self, first_name: str, is_alive=True):
        """Constructor of Stark class"""
        super().__init__(first_name, is_alive)
