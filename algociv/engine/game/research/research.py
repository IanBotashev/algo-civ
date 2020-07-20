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
    __required__ = None

    # The Energy cost
    __cost__ = None

    # Mutual Exclusive research. This means, you cannot research this, and anything included there.
    __mutually_exclusive_to__ = []

    # The Material Cost
    __material_cost__ = None

    # Traits to be edited.
    __traits__ = None


class SampleResearch(ResearchItem):
    __name__ = "Sample Research Item"
    __description__ = 'A Sample research item. Not meant to be in-game.'
    __required__ = []
    __mutually_exclusive_to__ = []

    __traits__ = {
        '__worker_dim__': Dimensions(5, 5),
        }


class SampleResearch1(ResearchItem):
    __name__ = "Sample Research Item 2"
    __description__ = 'A Sample research item 2. Not meant to be in-game.'
    __required__ = []
    __mutually_exclusive_to__ = [SampleResearch]

    __traits__ = {
        '__worker_dim__': Dimensions(7, 7),
        }
