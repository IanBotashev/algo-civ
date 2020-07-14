from algociv.engine.gravity.grid.assets import Dimensions


class TraitManager:
    def __init__(self):
        # Worker Default Stats
        self.__worker_dim__ = Dimensions(3, 3)

        # Structure Default Stats
        self.__structure_dim__ = Dimensions(3, 3)

        # Civilization Default Stats
        self.__civ_dim__ = Dimensions(5, 5)
