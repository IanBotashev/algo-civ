from algociv.engine.game.structures.building import Building
from algociv.engine.game.structures.worker import Worker
from algociv.engine.gravity.grid.assets import Coordinates, Unit
import inspect


class Actions:
    """
    All the actions civilizations can take use of
    """
    def __init__(self, gameinstance):
        self.__game__ = gameinstance

    def mine(self, building, unit: Unit):
        """
        Mines a unit, and puts the resources into the building inventory.
        :return:
        """
        building.__inventory__.append(unit.value.kwargs['material'])

    def initialize_building(self, building: Building, coordinates: Coordinates):
        """
        Initializes a building.
        :param structure:
        :param coordinates:
        :return:
        """

        # Apologies for this amount of errors, you may ignore this.
        # I had to do building() and not building.__init__(), because __init__ does not return the proper object instance.
        result = building(self.__game__.__traits__.__building_energy_cap__,
                            coordinates,
                            self.__game__.__traits__.__building_inventory_cap__,
                            self.__game__.__traits__.__building_module_cap__,
                            self.__game__.__traits__.__building_health__,
                            self.__game__.__traits__.__building_dim__,
                            self.__game__.__grid__,
                            self)

        self.__game__.__structures__.__buildings__.append(result)
        return result

    def initialize_worker(self, worker: Worker, coordinates: Coordinates):
        """
        Initializes a worker
        :param worker:
        :param coordinates:
        :return:
        """
        # Apologies for this amount of errors, you may ignore this.
        # I had to do worker() and not worker.__init__(), because __init__ does not return the proper object instance.
        result = worker(
            self.__game__.__traits__.__worker_module_cap__,
            self.__game__.__traits__.__worker_health__,
            self.__game__.__grid__,
            self.__game__.__traits__.__worker_dim__,
            coordinates)

        self.__game__.__structures__.__workers__.append(result)
        return result
