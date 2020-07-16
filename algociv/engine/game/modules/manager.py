from algociv.engine.game.modules.modules import Module
from algociv.engine.game.modules.errors import ModuleCapReached


class ModuleManager:
    def __init__(self, module_cap: int):
        self.__modules__ = []
        self.__cap__ = module_cap

    def add(self, module: Module):
        if len(self.__modules__) + 1 > self.__cap__:
            raise ModuleCapReached('The Module Capacity has been reached.')

        self.__modules__.append(module)

    def remove(self, module: Module):
        self.__modules__.remove(module)
