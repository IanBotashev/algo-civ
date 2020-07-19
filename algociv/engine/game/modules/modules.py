class Module:
    # The name of the module
    __name__ = None

    # The description of the module
    __description__ = None

    # The building cost. Basically, defines what materials this will cost
    __building_cost__ = None

    # The Energy Cost.
    __cost__ = None

    # The traits the module would edit
    __traits__ = None


class SampleModule:
    __name__ = "Sample Module"
    __description__ = "A Sample module. Not meant to be in-game"

    __traits__ = {
        "__can_mine__": True
    }
