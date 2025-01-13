from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class for characters
    """
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        next

    def die(self):
        self.is_alive = False


class Stark(Character):
    """
    Class for the Starks familly
    """
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
