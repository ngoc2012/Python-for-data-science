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
            self.vector = [x + object for x in self.vector]
            print(self.vector)
            return self.vector
        else:
            raise TypeError("object should be an integer or a float")

    def __mul__(self, object) -> None:
        """Multiplication operator"""
        if isinstance(object, int) or isinstance(object, float):
            self.vector = [x * object for x in self.vector]
            print(self.vector)
            return self.vector
        else:
            raise TypeError("object should be an integer or a float")

    def __sub__(self, object) -> None:
        """Subtraction operator"""
        if isinstance(object, int) or isinstance(object, float):
            self.vector = [x - object for x in self.vector]
            print(self.vector)
            return self.vector
        else:
            raise TypeError("object should be an integer or a float")

    def __truediv__(self, object) -> None:
        """Division operator"""
        if isinstance(object, int) or isinstance(object, float):
            if object == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            self.vector = [x / object for x in self.vector]
            print(self.vector)
            return self.vector
        else:
            raise TypeError("object should be an integer or a float")
