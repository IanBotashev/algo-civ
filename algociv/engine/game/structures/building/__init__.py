from algociv.engine.game.inventory import Inventory
from algociv.engine.gravity.grid.assets import Coordinates
from algociv.engine.game.modules.manager import ModuleManager


class Building:
    __structure_type__ = 'BUILDING'
    def __init__(self, energy_cap, location: Coordinates, inventory_cap, module_cap, health, dimensions, grid, actions):
        # This is getting extremely cluttered. I'm sure there's a better way of doing this. If you have a better way,
        # please post an issue about this.

        # Off limit variables
        self.__energy_cap__ = energy_cap
        self.__inventory__ = Inventory(inventory_cap)
        self.__coordinates__ = location
        self.__modules__ = ModuleManager(module_cap, self)
        self.__grid__ = grid
        self.__health__ = health
        self.__dimensions__ = dimensions

        # Ability variables
        self.__can_smelt__ = False
        self.__can_mine__ = False
        self.__can_produce_energy = False
        self.__can_craft__ = False

        # User accessible variables
        self.actions = actions
        self.scanned_units = []

    def run(self):
        print("Should probably put something here. Currently, your building is doing nothing.")

    def scan(self):
        """
        Basically uses generate() on __grid__
        :return:
        """
        self.scanned_units = self.__grid__.generate(self.__coordinates__, self.__dimensions__)

    def __repr__(self):
        return_string = \
            f"<Building(name: {self.__class__.__name__}, energy_cap: {self.__energy_cap__}, inventory: {self.__inventory__}, coordinates: {self.__coordinates__})>"

        return return_string
