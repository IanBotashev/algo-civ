class Seed:
    """
    A general seed, this is to make everything a bit tidier in the Grid
    """
    def __init__(self, seed, values: list, start_int: int, end_int: int, default):
        self.values = values
        self.seed = seed
        self.start = start_int
        self.end = end_int
        self.default = default

    def __repr__(self):
        return f"Seed(seed: {self.seed},values: {self.values})"
