from algociv.engine.game.modules.manager import ModuleManager


class Worker:
    def __init__(self, module_cap, health):
        self.__modules__ = ModuleManager(module_cap)
        self.__health__ = health

    def runtime(self):
        print('Should probably put something here. Currently, your worker is doing nothing!')
