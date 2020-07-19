from algociv.engine.game.structures.default import TraitManager
from algociv.engine.game.research.research import ResearchItem
from algociv.engine.game.research.errors import *


class ResearchManager:
    """
    This object keeps track of all researched building.
    """
    def __init__(self, trait_manager: TraitManager):
        self.__researched__ = []
        self.__available_research__ = []
        self.__traits__ = trait_manager

    def research(self, research: ResearchItem):
        """
        Researches a research item
        :param research:
        :return:
        """
        if self.check__available(research) and self.check_required(research) and self.check_if_special(research):
            self.update_traits(research.__traits__)
            self.update_research(research)

        else:
            raise ResearchNotAvailable("This cannot be researched, because a field has not been satisfied")

    def check_if_special(self, research: ResearchItem):
        """
        Checks if the specified research item's mutual exclusive list is valid
        :param research:
        :return:
        """
        return not any(item in self.__researched__ for item in research.__mutually_exclusive_to__)

    def check_required(self, research: ResearchItem):
        """
        Checks if a researches required item has already been researched.
        :param research:
        :return:
        """
        required = len(research.__required__)
        result = 0

        for _required in research.__required__:
            for _research in self.__researched__:
                if _research == _required:
                    result += 1

        if result == required:
            return True

        else:
            return False

    def check__available(self, research: ResearchItem):
        """
        Checks if you can research an RI
        :param research:
        :return:
        """
        for _research in self.__available_research__:
            if _research == research:
                return True

        return False

    def update_research(self, research: ResearchItem):
        """
        Updates __available_research__ and __researched__
        :param research:
        :return:
        """
        self.__available_research__.remove(research)
        self.__researched__.append(research)

    def update_traits(self, traits):
        """
        Updates the trait manager
        :param traits:
        :return:
        """
        for key in traits:
            self.__traits__.__dict__[key] = traits[key]
