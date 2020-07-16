from algociv.engine.game.objects.structures import Structure
from algociv.engine.game.objects.worker import Worker
from algociv.engine.gravity.grid.assets import Coordinates
from algociv.engine.game.objects.default import TraitManager
from algociv.engine.game.objects.manager import ObjectManager


class Actions:
    """
    All the actions civilizations can take use of
    """
    def __init__(self, grid, traits: TraitManager, objects: ObjectManager):
        self.__grid__ = grid
        self.__traits__ = traits
        self.__objects__ = objects

    def initialize_structure(self, structure: Structure, coordinates: Coordinates):
        """
        Initializes a structure.
        :param structure:
        :return:
        """
        result = structure(self.__traits__.__structure_energy_cap__,
                                    coordinates,
                                    self.__traits__.__structure_inventory_cap__,
                                    self.__traits__.__structure_module_cap__,
                                    self.__traits__.__structure_health__,
                                    self.__traits__.__structure_dim__,
                                    self.__grid__)

        self.__objects__.__structures__.append(result)
        return result

    def initialize_worker(self, worker: Worker, coordinates: Coordinates):
        """
        Initializes a worker
        :param worker:
        :return:
        """
        result = worker.__init__(
            self.__traits__.__worker_module_cap__,
            self.__traits__.__worker_health__,
            self.__grid__,
            self.__traits__.__worker_dim__,
            coordinates)

        self.__objects__.__workers__.append(result)
        return result
