from algociv.engine.game.modules.modules import Module
from algociv.engine.game.modules.errors import ModuleCapReached


class ModuleManager:
    def __init__(self, module_cap: int, structure):
        self.__modules__ = []
        self.__cap__ = module_cap
        self.__structure__ = structure

    def add(self, module: Module):
        if len(self.__modules__) + 1 > self.__cap__:
            raise ModuleCapReached('The Module Capacity has been reached.')

        self.edit_traits(module.__traits__)
        self.__modules__.append(module)

    def edit_traits(self, traits):
        """
        Edits the traits of the given structure
        :param traits:
        :return:
        """
        for key in traits:
            self.__structure__.__dict__[key] = traits[key]

    def revert_traits(self, traits):
        """
        Reverts specific stats back to their default state
        :param traits:
        :return:
        """
        for key in traits:
            self.__structure__.__dict__[key] = not traits[key]

    def remove(self, module: Module):
        self.revert_traits(module.__traits__)
        self.__modules__.remove(module)
