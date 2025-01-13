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
    """Your docstring for Class"""
    def __init__(self, name, is_alive=True):
        self.name = name
        self.is_alive = is_alive
    #your code here
