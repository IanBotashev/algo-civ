from algociv.engine.gravity.grid.assets import Value
from algociv.engine.gravity.grid.generation.seed import Seed
from algociv.engine.game.game.actions import *
from algociv.engine.game.structures.manager import StructureManager
from algociv.engine.game.research.manager import ResearchManager
from algociv.engine.game.structures.civilization import Civilization
from algociv.engine.game.structures.default import TraitManager
from algociv.engine.game.research.research import SampleResearch
from algociv.engine.game.items.materials import *
from algociv.engine.gravity.grid import Grid
import logging
import random


class Game:
    def __init__(self, algorithm):
        self.__materials__ = [
            Value('Stone', (-0.2, 0.0), material=Stone),
            ]

        self.__seed__ = Seed(random.randint(100000, 999999),
                             self.__materials__,
                             Value('Dirt', (0, 0), material=Dirt))
        self.__grid__ = Grid(self.__seed__, logging.DEBUG)

        self.__traits__ = TraitManager()
        self.actions = Actions(self)

        self.__structures__ = StructureManager()
        self.__civ__ = Civilization(self.__grid__,
                                    Coordinates(0, 0),
                                    self.actions,
                                    self.__traits__)

        self.__research__ = ResearchManager(self,
                                            self.__traits__)
        self.add_allowed_research()

        self.algo = algorithm(self.__civ__)

    def add_allowed_research(self):
        """
        Adds all allowed research
        :return:
        """
        research = [
            SampleResearch,
        ]
        self.__research__.__available_research__ = research

    def run_structures(self):
        """
        Runs all building
        :return:
        """
        for building in self.__structures__.__buildings__:
            building.run()

    def run_workers(self):
        """
        Runs all workers
        :return:
        """
        for worker in self.__structures__.__workers__:
            worker.run()

    def run(self):
        self.algo.run()
        self.run_structures()
        self.run_workers()
