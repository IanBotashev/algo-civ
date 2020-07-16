from algociv.engine.gravity.grid.assets import Value
from algociv.engine.gravity.grid.generation.seed import Seed
from algociv.engine.game.game.actions import *
from algociv.engine.game.objects.manager import ObjectManager
from algociv.engine.game.research.manager import ResearchManager
from algociv.engine.game.research.research import *
from algociv.engine.game.objects.default import TraitManager
from algociv.engine.game.research.research import SampleResearch
from algociv.engine.gravity.grid import Grid
import random


class Game:
    def __init__(self):
        self.__materials__ = [
            Value('Stone', [40, 41, 42, 43, 44, 45, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]),
            Value('Coal', [46, 47, 48, 49, 50]),
            Value('Iron', [21, 22, 24, 26, 28, 95]),
            Value('Copper', [97, 96, 67]),
            Value('Platinum', [10]),
            Value('Orsium', [2]),
            Value("Diamond", [1]),
            ]

        self.__seed_num__ = random.randint(100000, 999999)
        self.__seed__ = Seed(self.__seed_num__, self.__materials__, 1, 105,  Value('Dirt', []))
        self.__grid__ = Grid(self.__seed__)

        self.__traits__ = TraitManager()
        self.__objects__ = ObjectManager(self.__grid__, self.__traits__)

        self.actions = Actions(self.__grid__, self.__traits__, self.__objects__)

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
        Runs all structures
        :return:
        """
        for structure in self.__objects__.__structures__:
            structure.runtime()

    def run_workers(self):
        """
        Runs all workers
        :return:
        """
        for worker in self.__objects__.__workers__:
            worker.runtime()

    def runtime(self):
        self.run_structures()
        self.run_workers()
