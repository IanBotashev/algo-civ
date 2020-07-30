from algociv.engine.game.inventory import Inventory
from algociv.engine.gravity.grid.assets import Coordinates
from algociv.engine.game.modules.manager import ModuleManager
from algociv.engine.game.structures.default import TraitManager


class Civilization:
    __structure_type__ = 'CIV'

    def __init__(self, grid, location: Coordinates, actions, traits: TraitManager):
        # Off limit variables
        self.__traits__ = traits

        self.__modules__ = ModuleManager(self.__traits__.__civ__['module_cap'], self)
        self.__energy_cap__ = self.__traits__.__civ__["energy_cap"]
        self.__health_cap__ = self.__traits__.__civ__['health_cap']
        self.__dimensions__ = self.__traits__.__civ__["dimensions"]
        self.__inventory__ = Inventory(self.__traits__.__civ__['inventory_cap'])
        self.__grid__ = grid
        self.__coordinates__ = location

        # User Accessible Variables
        self.health = self.__traits__.__civ__['health_cap']
        self.energy = self.__traits__.__civ__['energy_cap']
        self.actions = actions
        self.scanned_units = []

        # Ability variables
        self.__can_smelt__ = True
        self.__can_mine__ = True
        self.__can_produce_energy = True
        self.__can_craft__ = True

    def run(self):
        print("Should probably put something here. Currently, your building is doing nothing.")

    def update(self):
        """
        Updates traits for this instance of the object.
        :return:
        """
        self.__energy_cap__ = self.__traits__.__civ__['energy_cap']
        self.__health_cap__ = self.__traits__.__civ__['health_cap']
        self.__inventory__.slots = self.__traits__.__civ__["inventory_cap"]
        self.__modules__.__cap__ = self.__traits__.__civ__["module_cap"]
        self.__dimensions__ = self.__traits__.__civ__['dimensions']
        self.__health__ = self.__traits__.__civ__['health_cap']

        for module in self.__modules__.__modules__:
            self.__modules__.edit_traits(module.__traits__)


    def scan(self):
        """
        Basically uses generate() on __grid__
        :return:
        """
        self.scanned_units = self.__grid__.generate(self.__coordinates__, self.__dimensions__)

    def __repr__(self):
        return_string = \
            f"<Civ(name: {self.__class__.__name__}, energy_cap: {self.__energy_cap__}, inventory: {self.__inventory__}, coordinates: {self.__coordinates__})>"

        return return_string