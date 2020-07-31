from algociv.engine.game.items.materials import Structure
from algociv.engine.gravity.grid import Grid
from algociv.engine.gravity.grid.assets import Unit, Coordinates
from algociv.engine.gravity.grid.value import Value


def is_mineable(material, mineables):
    """
    Checks if a material is mineable
    :param material:
    :param mineables:
    :return:
    """
    return material in mineables

def check_required_materials(required_mats, owned_mats):
    """
    Checks if the user has the required materials to craft something.
    :param required_mats:
    :param owned_mats:
    :return:
    """
    return all(item in owned_mats for item in required_mats)


def is_craftable(item, craftables):
    """
    Checks if an item is craftable
    :param item:
    :param craftables:
    :return:
    """
    return item in craftables


def build_structure_on_grid(structure, coordinates, grid: Grid):
    """
    Uses the material "structure-type" and puts it down on a grid.
    :param structure:
    :param coordinates:
    :param grid:
    :return:
    """
    structure_ = Structure()
    structure_.__structure__ = structure
    grid.update_saved_units(Unit(Value('Structure', (0, 0), structure=structure_), coordinates))
