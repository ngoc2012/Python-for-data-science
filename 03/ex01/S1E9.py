from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for characters"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Constructor of Character class"""
        next

    def die(self):
        """Method to kill a character"""
        self.is_alive = False


class Stark(Character):
    """Class for the Starks familly"""
    def __init__(self, first_name, is_alive=True):
        """Constructor of Stark class"""
        self.first_name = first_name
        self.is_alive = is_alive
