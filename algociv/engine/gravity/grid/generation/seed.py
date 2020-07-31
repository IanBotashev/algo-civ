class Seed:
    """
    A general seed, this is to make everything a bit tidier in the Grid
    """
    def __init__(self, seed, values: list, default):
        self.values = values
        self.seed = seed
        self.default = default

        # Simplex Noise config
        self.scale = 100.0
        self.octaves = 16
        self.persistence = 0.5
        self.lacunarity = self.octaves * 16.0

    def __repr__(self):
        return f"Seed(seed: {self.seed},values: {self.values})"
