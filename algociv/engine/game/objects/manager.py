from algociv.engine.gravity.grid.assets import Dimensions
from algociv.engine.game.game.actions import *


class ObjectManager:
    def __init__(self, grid, traitmanager):
        self.__structures__ = []
        self.__workers__ = []
        self.__grid__ = grid
        self.__default__ = traitmanager


    def create_structure(self, structure, coordinates):
        """
        Creates a new structure.
        :param structure:
        :return:
        """
        new_structure = initialize_structure(structure, self.__grid__, self.__default__.__structure_dim__, coordinates)
        self.__structures__.append(new_structure)

    def create_worker(self, worker, coordinates):
        """
        Creates a new structure
        :param worker:
        :return:
        """
        new_worker = initialize_worker(worker, self.__grid__, self.__default__.__worker_dim__, coordinates)
        self.__workers__.append(new_worker)
