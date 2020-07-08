class Seed:
    """
    A general seed, this is to make everything a bit tidier in the Grid
    """
    def __init__(self, seed, values: list, length: int, width: int):
        self.values = values
        self.length = length
        self.width = width
        self.seed = seed

    def __repr__(self):
        return f"Seed(seed: {self.seed},values: {self.values}, width: {self.width}, length: {self.length})"
