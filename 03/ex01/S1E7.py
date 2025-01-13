from S1E9 import Character


class Baratheon(Character):
    """Class for the Baratheon familly"""
    def __init__(self, first_name, is_alive=True):
        """Constructor of Baratheon class"""
        self.first_name = first_name
        self.is_alive = is_alive


class Lannister(Character):
    """Class for the Lannister familly"""
    def __init__(self, first_name, is_alive=True):
        """Constructor of Lannister class"""
        self.first_name = first_name
        self.is_alive = is_alive
    
    @classmethod
    def create_lannister(cls, first_name, is_alive):
        obj = cls(first_name, is_alive)
        return cls(first_name, is_alive)
    #your code here