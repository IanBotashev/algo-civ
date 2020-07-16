from algociv.engine.game.inventory import Inventory
from algociv.engine.gravity.grid.assets import Coordinates
from algociv.engine.game.modules.manager import ModuleManager


class Structure:
    def __init__(self, energy_cap, location: Coordinates, inventory_cap, module_cap, health, dimensions, grid):
        self.__energy_cap__ = energy_cap
        self.__inventory__ = Inventory(inventory_cap)
        self.__coordinates__ = location
        self.__modules__ = ModuleManager(module_cap)
        self.__grid__ = grid
        self.__health__ = health
        self.__dimensions__ = dimensions
        self.scanned_units = []
        self.scan()

    def runtime(self):
        print("Should probably put something here. Currently, your structure is doing nothing.")

    def scan(self):
        """
        Basically uses generate() on __grid__
        :return:
        """
        self.scanned_units = self.__grid__.generate(self.__coordinates__, self.__dimensions__)

    def __repr__(self):
        return_string = \
        f"<Structure(name: {self.__class__.__name__}, energy_cap: {self.__energy_cap__}, inventory: {self.__inventory__}, coordinates: {self.__coordinates__})>"

        return return_string
