from algociv.engine.game.inventory import Inventory
from algociv.engine.gravity.grid.assets import Coordinates


class Structure:
    def __init__(self, energy_cap, location: Coordinates):
        self.ENERGY_CAP = energy_cap
        self.INVENTORY = Inventory()
        self.LOCATION = location

    def runtime(self):
        print("Should probably put something here. Currently, your structure is doing nothing.")

    def __repr__(self):
        return_string = \
        f"<Structure(name: {self.__class__.__name__}, energy_cap: {self.ENERGY_CAP}, inventory: {self.INVENTORY}, location: {self.LOCATION})>"

        return return_string
