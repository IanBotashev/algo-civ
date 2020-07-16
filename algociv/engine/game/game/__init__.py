from algociv.engine.gravity.grid.assets import Value
from algociv.engine.gravity.grid.generation.seed import Seed
from algociv.engine.game.game.actions import *
from algociv.engine.game.structures.manager import StructureManager
from algociv.engine.game.research.manager import ResearchManager
from algociv.engine.game.research.research import *
from algociv.engine.game.structures.default import TraitManager
from algociv.engine.game.research.research import SampleResearch
from algociv.engine.game.items.materials import *
from algociv.engine.gravity.grid import Grid
import random


class Game:
    def __init__(self):
        self.__materials__ = [
            Value('Stone', [40, 41, 42, 43, 44, 45, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], material=Stone),
            ]

        self.__seed_num__ = random.randint(100000, 999999)
        self.__seed__ = Seed(self.__seed_num__, self.__materials__, 1, 105,  Value('Dirt', [], material=Dirt))
        self.__grid__ = Grid(self.__seed__)

        self.__structures__ = StructureManager()

        self.__traits__ = TraitManager()
        self.actions = Actions(self)

        self.__research__ = ResearchManager(self.__traits__)
        self.add_allowed_research()

    def add_allowed_research(self):
        """
        Adds all allowed research
        :return:
        """
        research = [
            SampleResearch,
            SampleResearch1
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
        self.run_structures()
        self.run_workers()
