from algociv.engine.gravity.grid.assets import Value
from algociv.engine.gravity.grid.generation.seed import Seed
from algociv.engine.game.game.actions import *
from algociv.engine.game.objects.manager import ObjectManager
from algociv.engine.game.research.manager import ResearchManager
from algociv.engine.game.research.research import *
from algociv.engine.game.objects.default import TraitManager
import random


class Game:
    def __init__(self):
        self.__materials__ = [
            Value('Stone', [40, 41, 42, 43, 44, 45]),
            ]
        self.__seed__ = Seed(random.randint(100000, 999999), self.__materials__, 1, 105,  Value('Dirt', []))
        self.__grid__ = Grid(self.__seed__)

        self.__traits__ = TraitManager()
        self.__objects__ = ObjectManager(self.__grid__, self.__traits__)
        self.__research__ = ResearchManager(self.__traits__)

    def add_allowed_research(self):
        """
        Adds all allowed research
        :return:
        """
        research = [
            SampleResearch()
        ]
        self.__research__.__allowed_research__ = research

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
