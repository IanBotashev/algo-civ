from AlgoCiv.engine.gravity.grid.generation import *
from AlgoCiv.engine.gravity.grid.generation.seed import *
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
    def __init__(self, seed: Seed, center_point: Coordinates, logging_level=logging.INFO):
        self.seed = seed
        self.center_point = center_point
        self.logging_level = logging_level
        start_logging(self.logging_level)

        self.saved_units = []
        self.picklist = generate_picklist(seed.values)
    def add_value(self, value: Value):
        """
        Adds a new value into the self.values list.
        :param value:
        :return:
        """
        self.seed.values.append(value)
        logging.debug(f"Added new value: {value}")

    def generate(self):
        """
        Generates all units around the center point.
        :return:
        """
        self.visible_units = generate_visible_units(self.center_point, self.seed)
        self.loaded_units = generate_units(self.seed, self.visible_units, self.saved_units, self.picklist)
