from algociv.engine.gravity.grid.assets import Dimensions


class ResearchItem:
    """
    The metaclass for all research items
    """

    # Name given to the algorithm. Only for aesthetic purposes.
    __external_name__ = None

    # Name only used internally. Must be formatted, so there's no special characters, and it must be fully uppercase
    __internal_name__ = None

    # Description. Information given to the user
    __description__ = None

    # This shows the game what research is required so this can be researched
    __required__ = None

    # Traits to be edited.
    __traits__ = None


class SampleResearch(ResearchItem):
    __external_name__ = "Sample Research Item"
    __internal_name__ = "SAMPLERESEARCHITEM"
    __description__ = 'A Sample research item. Not meant to be in-game.'
    __required__ = None

    __traits__ = {
        '__worker_dim__': Dimensions(5, 5),
        }
