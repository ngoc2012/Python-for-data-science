from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class for characters
    """
    def __init__(self, name, is_alive=True):
        self.name = name
        self.is_alive = is_alive

    @abstractmethod
    def set_alive(self, is_alive):
        self.is_alive = is_alive


class Stark(Character):
    """Your docstring for Class"""
    #your code here
