from algociv.engine.game.inventory import Inventory
from algociv.engine.gravity.grid.assets import Coordinates
from algociv.engine.game.modules.manager import ModuleManager
from algociv.engine.game.structures.default import TraitManager


class Building:
    __structure_type__ = 'BUILDING'

    def __init__(self, grid, location: Coordinates, actions, traits: TraitManager):
        # This is getting extremely cluttered. I'm sure there's a better way of doing this. If you have a better way,
        # please post an issue about this.

        # Off limit variables
        self.__traits__ = traits
        self.__energy_cap__ = self.__traits__.__buildings__['energy_cap']
        self.__inventory__ = Inventory(self.__traits__.__buildings__["inventory_cap"])
        self.__coordinates__ = location
        self.__modules__ = ModuleManager(self.__traits__.__buildings__["module_cap"], self)
        self.__grid__ = grid
        self.__health__ = self.__traits__.__buildings__['health']
        self.__dimensions__ = self.__traits__.__buildings__['dimensions']

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

    def update(self):
        """
        Updates traits for this instance of the object.
        :return:
        """
        self.__energy_cap__ = self.__traits__.__buildings__['energy_cap']
        self.__inventory__.slots = self.__traits__.__buildings__["inventory_cap"]
        self.__modules__.__cap__ = self.__traits__.__buildings__["module_cap"]
        self.__dimensions__ = self.__traits__.__buildings__['dimensions']

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
