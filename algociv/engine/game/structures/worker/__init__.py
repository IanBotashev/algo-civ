from algociv.engine.game.modules.manager import ModuleManager
from algociv.engine.gravity.grid import Grid
from algociv.engine.gravity.grid.assets import Coordinates
from algociv.engine.game.inventory import Inventory
from algociv.engine.game.structures.default import TraitManager


class Worker:
    __structure_type__ = 'WORKER'

    def __init__(self, grid: Grid, coordinates: Coordinates, actions, traits: TraitManager):
        # Off Limit Variables
        self.__traits__ = traits

        self.__modules__ = ModuleManager(self.__traits__.__workers__['module_cap'], self)
        self.__energy_cap__ = self.__traits__.__workers__["energy_cap"]
        self.__health_cap__ = self.__traits__.__workers__['health_cap']
        self.__dimensions__ = self.__traits__.__workers__["dimensions"]
        self.__inventory__ = Inventory(self.__traits__.__workers__['inventory_cap'])
        self.__grid__ = grid
        self.__coordinates__ = coordinates

        # User Accessible Variables
        self.health = self.__traits__.__workers__["health_cap"]
        self.energy = self.__traits__.__workers__['energy_cap']
        self.actions = actions

        # Ability variables
        self.__can_smelt__ = False
        self.__can_mine__ = False
        self.__can_produce_energy = False
        self.__can_craft__ = False

    def run(self):
        print('Should probably put something here. Currently, your worker is doing nothing!')

    def update(self):
        """
        Updates traits for this instance of the object.
        :return:
        """
        self.__modules__.__cap__ = self.__traits__.__workers__['module_cap']
        self.__energy_cap__ = self.__traits__.__workers__["energy_cap"]
        self.__dimensions__ = self.__traits__.__workers__["dimensions"]
        self.__health_cap__ = self.__traits__.__workers__['health_cap']
        self.__inventory__.slots = self.__traits__.__workers__['inventory_cap']

        for module in self.__modules__.__modules__:
            self.__modules__.edit_traits(module.__traits__)


    def __repr__(self):
        return_string = \
            f"<Worker(name: {self.__class__.__name__}, energy_cap: {self.__energy_cap__}, inventory: {self.__inventory__}, coordinates: {self.__coordinates__})>"

        return return_string
