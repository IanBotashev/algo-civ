from algociv.engine.game.modules.manager import ModuleManager
from algociv.engine.gravity.grid import Grid
from algociv.engine.gravity.grid.assets import Coordinates, Dimensions


class Worker:
    def __init__(self, module_cap, health, grid: Grid, dimensions: Dimensions, coordinates: Coordinates):
        self.__modules__ = ModuleManager(module_cap)
        self.__health__ = health
        self.__grid__ = grid
        self.__dimensions__ = dimensions
        self.__coordinates__ = coordinates
        self.scanned_units = []
        self.scan()

    def runtime(self):
        print('Should probably put something here. Currently, your worker is doing nothing!')

    def scan(self):
        """
        Basically uses generate() on __grid__
        :return:
        """
        self.scanned_units = self.__grid__.generate(self.__coordinates__, self.__dimensions__)
