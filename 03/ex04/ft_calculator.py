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
        print("Dot product is:", sum([V1[i] * V2[i] for i in range(len(V1))]))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        print("Add Vector is :", [float(V1[i] + V2[i]) for i in range(len(V1))])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print("Sous Vector is:", [float(V1[i] - V2[i]) for i in range(len(V1))])