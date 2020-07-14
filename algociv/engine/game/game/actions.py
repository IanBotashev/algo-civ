from algociv.engine.game.objects.structures import Structure
from algociv.engine.game.objects.worker import Worker
from algociv.engine.gravity.grid.assets import Coordinates, Dimensions
from algociv.engine.gravity.grid import Grid


def initialize_structure(structure: Structure, grid: Grid, dimensions: Dimensions, coordinates: Coordinates):
    """
    Initializes a structure.
    :param structure:
    :return:
    """
    result = structure(100, coordinates, 5, 5, 10)
    return result

def initialize_worker(worker: Worker, grid: Grid, dimensions: Dimensions, coordinates: Coordinates):
    """
    Initializes a worker
    :param worker:
    :return:
    """
    result = worker(2, 100, grid, dimensions, coordinates)
    return result
