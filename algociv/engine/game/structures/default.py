from algociv.engine.gravity.grid.assets import Dimensions
from algociv.engine.game.items.items import *
from algociv.engine.game.items.materials import *
from algociv.engine.game.research.research import Trait


class TraitManager:
    def __init__(self):
        # All the craftable items
        self.__craftables__ = [
            SampleItem,
        ]

        # All the mineable materials
        self.__mineables__ = [
            Dirt,
        ]

        # Worker Default Stats
        self.__workers__ = {
            "dimensions": Dimensions(3, 3),
            "health_cap": 50,
            "module_cap": 2,
            "energy_cap": 50,
            "inventory_cap": 5,
        }

        # Building Default Stats
        self.__buildings__ = {
            "dimensions": Dimensions(3, 3),
            "health_cap": 75,
            "module_cap": 2,
            "energy_cap": 100,
            "inventory_cap": 10,
        }

        # Civilization Default Stats
        self.__civ__ = {
            "dimensions": Dimensions(5, 5),
            "health_cap": 100,
            "module_cap": 4,
            "energy_cap": 200,
            "inventory_cap": 20,
        }


    def update(self, trait: Trait):
        self.__dict__[trait.structure][trait.trait] = trait.value
