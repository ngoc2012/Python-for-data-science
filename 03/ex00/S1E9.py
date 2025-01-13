from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class for characters
    """
    @abstractmethod
    def __init__(self, name, is_alive=True):
        next

    def set_die(self):
        self.is_alive = False


class Stark(Character):
    """
    Class for the Starks familly
    """
    def __init__(self, name, is_alive=True):
        self.name = name
        self.is_alive = is_alive
