class calculator:
    """Calculator class for a vector"""
    def __init__(self, vector: list):
        """Constructor of calculator class"""
        if not isinstance(vector, list):
            raise TypeError("vector should be a list")
        if len(vector) == 0:
            raise ValueError("vector should not be empty")
        self.vector = vector

    def __add__(self, object) -> None:
        """Addition operator"""
        if isinstance(object, int) or isinstance(object, float):
            return self.vector + object

    def __mul__(self, object) -> None:
        """Multiplication operator"""
        if isinstance(object, int) or isinstance(object, float):
            return self.vector * object

    def __sub__(self, object) -> None:
        """Subtraction operator"""
        if isinstance(object, int) or isinstance(object, float):
            return self.vector - object

    def __truediv__(self, object) -> None:
        """Division operator"""
        if isinstance(object, int) or isinstance(object, float):
            if object == 0:
                return None
            return self.vector / object
