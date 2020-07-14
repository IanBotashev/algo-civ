from algociv.engine.game.inventory import Inventory


class Civilization:
    def __init__(self):
        self.KNOWN_METALS = []
        self.__inventory__ = Inventory(20)
        self.__energy__ = 100
