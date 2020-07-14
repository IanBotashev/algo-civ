from algociv.engine.gravity.grid.assets import Value


class Game:
    def __init__(self):
        self.__materials__ = [
            Value('Dirt', 40),
            Value('Stone', 30),
            ]
        self.__structures__ = []
        self.__workers__ = []
