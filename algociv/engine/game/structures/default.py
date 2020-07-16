from algociv.engine.gravity.grid.assets import Dimensions


class TraitManager:
    def __init__(self):
        # Worker Default Stats
        self.__worker_dim__ = Dimensions(3, 3)
        self.__worker_health__ = 50
        self.__worker_module_cap__ = 2
        self.__worker_energy_cap__ = 50
        self.__worker_inventory_cap__ = 5

        # Structure Default Stats
        self.__building_dim__ = Dimensions(3, 3)
        self.__building_health__ = 75
        self.__building_module_cap__ = 2
        self.__building_energy_cap__ = 100
        self.__building_inventory_cap__ = 10

        # Civilization Default Stats
        self.__civ_dim__ = Dimensions(5, 5)
        self.__civ_health__ = 100
        self.__civ_module_cap__ = 4
        self.__civ_energy_cap__ = 200
        self.__civ_inventory_cap__ = 20
