from algociv.engine.gravity.grid.generation import *
from algociv.engine.gravity.grid.generation.seed import *
import logging


def start_logging(logging_level):
    """
    Starts logging.
    :param logging_level:
    :return:
    """
    logging.basicConfig(format='%(levelname)s:%(asctime)s %(message)s', filemode='w', filename='grid.log', level=logging_level)
    logging.info(f'Started Logging, Level : {logging_level}')


class Grid:
    """
    Classic Grid.
    """
    def __init__(self, seed: Seed, logging_level=logging.INFO):
        self.seed = seed
        self.logging_level = logging_level
        start_logging(self.logging_level)

        self.saved_units = []

    def generate(self, point: Coordinates, dimensions: Dimensions):
        """
        Generates all units around the center point.
        :return:
        """
        visible_units = generate_visible_units(point, dimensions)
        return generate_units(self.seed, visible_units, self.saved_units, dimensions)
