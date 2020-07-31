from algociv.engine.gravity.grid.generation.seed import *
from algociv.engine.gravity.grid.assets import Coordinates, Dimensions
from algociv.engine.gravity.grid.generation import *
import logging
from algociv.engine.gravity.grid.generation import pick_value


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

        self.saved_units = {

        }

    def generate(self, point: Coordinates, dimensions: Dimensions):
        """
        Generates all units around the center point.
        :return:
        """
        visible_units = generate_visible_units(point, dimensions)
        return generate_units(visible_units, self, dimensions)

    def update_saved_units(self, unit: Unit):
        """
        Updates/adds a saved unit into the saved_units.
        :param unit:
        :return:
        """
        self.saved_units.update({(unit.coordinates.xpos, unit.coordinates.ypos): unit.value})

    def delete_saved_unit(self, coordinates):
        """
        Deletes a unit from the saved_units dictionary.
        Also can be used to reset units.
        :param coordinates:
        :return:
        """
        del self.saved_units[(coordinates.xpos, coordinates.ypos)]

