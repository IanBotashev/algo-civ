from algociv.engine.game.inventory import Inventory
from algociv.engine.gravity.grid.assets import Coordinates
from algociv.engine.game.modules.manager import ModuleManager


class Structure:
    def __init__(self, energy_cap, location: Coordinates, inventory_cap, module_cap, health, dimensions):
        self.__energy_cap__ = energy_cap
        self.__inventory__ = Inventory(inventory_cap)
        self.__location__ = location
        self.__modules__ = ModuleManager(module_cap)
        self.__health__ = health
        self.__dimensions__ = dimensions

    def runtime(self):
        print("Should probably put something here. Currently, your structure is doing nothing.")

    def __repr__(self):
        return_string = \
        f"<Structure(name: {self.__class__.__name__}, energy_cap: {self.__energy_cap__}, inventory: {self.__inventory__}, location: {self.__location__})>"

        return return_string
