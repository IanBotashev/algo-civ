from algociv.engine.game.modules.manager import ModuleManager
from algociv.engine.gravity.grid import Grid
from algociv.engine.gravity.grid.assets import Coordinates, Dimensions
from algociv.engine.game.inventory import Inventory


class Worker:
    __structure_type__ = 'WORKER'
    def __init__(self, module_cap, health, grid: Grid, dimensions: Dimensions, coordinates: Coordinates, actions, energy_cap, inventory_cap):
        self.__modules__ = ModuleManager(module_cap, self)
        self.__health__ = health
        self.__grid__ = grid
        self.__energy_cap__ = energy_cap
        self.__dimensions__ = dimensions
        self.__coordinates__ = coordinates
        self.__inventory__ = Inventory(inventory_cap)

        self.actions = actions
        self.scanned_units = []

        # Ability variables
        self.__can_smelt__ = False
        self.__can_mine__ = False
        self.__can_produce_energy = False
        self.__can_craft__ = False

    def runtime(self):
        print('Should probably put something here. Currently, your worker is doing nothing!')

    def scan(self):
        """
        Basically uses generate() on __grid__
        :return:
        """
        self.scanned_units = self.__grid__.generate(self.__coordinates__, self.__dimensions__)

    def __repr__(self):
        return_string = \
            f"<Worker(name: {self.__class__.__name__}, energy_cap: {self.__energy_cap__}, inventory: {self.__inventory__}, coordinates: {self.__coordinates__})>"

        return return_string
