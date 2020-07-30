from algociv.engine.gravity.grid.assets import Dimensions


class ResearchItem:
    """
    The metaclass for all research items
    """

    # Name given to the algorithm. Only for aesthetic purposes.
    __name__ = None

    # Description. Information given to the user
    __description__ = None

    # This shows the game what research is required so this can be researched
    __required__ = []

    # The Energy cost
    __cost__ = None

    # Mutual Exclusive research. This means, you cannot research this, and anything included there.
    __mutually_exclusive_to__ = []

    # The Material Cost
    __material_cost__ = []

    # Traits to be edited.
    __traits__ = []


class Trait:
    """
    This is an object to carry what traits need to be updated once a research has been done.
    """
    def __init__(self, structure, trait, value, **kwargs):
        self.structure = structure
        self.trait = trait
        self.value = value
        self.kwargs = kwargs

    def __repr__(self):
        return f"<Trait(structure: {self.structure}, trait: {self.trait}, value: {self.value})>"


class SampleResearch(ResearchItem):
    __name__ = "Sample Research Item"
    __description__ = 'A Sample research item. Not meant to be in-game.'
    __required__ = []
    __cost__ = 10
    __mutually_exclusive_to__ = []

    __traits__ = [
        Trait('__workers__', "health_cap", 1000),
        ]
