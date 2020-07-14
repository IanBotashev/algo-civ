from algociv.engine.game.objects.default import TraitManager
from algociv.engine.game.research.research import ResearchItem


class ResearchManager:
    """
    This object keeps track of all researched objects.
    """
    def __init__(self, trait_manager: TraitManager):
        self.__researched__ = []
        self.__allowed_research__ = []
        self.__traits__ = trait_manager

    def research(self, research: ResearchItem):
        """
        Researches a research item
        :param research:
        :return:
        """
        self.update_traits(research.__traits__)

    def update_traits(self, traits):
        """
        Updates the trait manager
        :param traits:
        :return:
        """
        for key in traits:
            self.__traits__.__dict__[key] = traits[key]
