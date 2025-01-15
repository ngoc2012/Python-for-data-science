class calculator:
    """Calculator class for a vector"""
    def __init__(self, vector: list):
        """Constructor of calculator class"""
        if not isinstance(vector, list):
            raise TypeError("vector should be a list")
        if len(vector) == 0:
            raise ValueError("vector should not be empty")
        self.vector = vector

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        x = sum([V1[i] * V2[i] for i in range(len(V1))])
        print("Dot product is: ", x)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
    #your code here

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
    #your code here