from algociv.engine.game.objects.structures import Structure
from algociv.engine.game.objects.worker import Worker
from algociv.engine.game.game import Game
from algociv.engine.gravity.grid.assets import Coordinates


class Actions:
    """
    All the actions civilizations can take use of
    """
    def __init__(self, gameinstance: Game):
        self.__game__ = gameinstance

    def initialize_structure(self, structure: Structure, coordinates: Coordinates):
        """
        Initializes a structure.
        :param structure:
        :param coordinates:
        :return:
        """

        # Apologies for this amount of errors, you may ignore this.
        # I had to do structure() and not structure.__init__(), because __init__ does not return the proper object instance.
        result = structure(self.__game__.__traits__.__structure_energy_cap__,
                                    coordinates,
                                    self.__game__.__traits__.__structure_inventory_cap__,
                                    self.__game__.__traits__.__structure_module_cap__,
                                    self.__game__.__traits__.__structure_health__,
                                    self.__game__.__traits__.__structure_dim__,
                                    self.__game__.__grid__)

        self.__game__.__objects__.__structures__.append(result)
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

        self.__game__.__objects__.__workers__.append(result)
        return result
