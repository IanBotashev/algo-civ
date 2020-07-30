class DoesNotHaveRequiredItems(Exception):
    pass


class NotCraftable(Exception):
    pass


class NotMineable(Exception):
    pass


class CannotMine(Exception):
    pass


class CannotCraft(Exception):
    pass


class CannotProduceEnergy(Exception):
    pass


class MissingMaterials(Exception):
    pass


class NotEnoughEnergy(Exception):
    pass


class InvalidStructureType(Exception):
    pass


class ReachedCap(Exception):
    pass
