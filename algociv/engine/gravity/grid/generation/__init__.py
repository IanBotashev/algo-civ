from AlgoCiv.engine.gravity.grid.assets import *
from AlgoCiv.engine.gravity.grid.value import *
import random
import logging


"""
This is the system responsible for generating the grids.
"""


def generate_visible_units(center_point, seed):
    """
    Generates a list of all visible units.
    It does not return a list of Unit objects, but coordinate objects.
    :param center_point:
    :param width:
    :param height:
    :return:
    """
    result = []
    origin_point = Coordinates(center_point.xpos-1, center_point.ypos-1)
    logging.info('Generating visible units...')
    for y in range(seed.length):
        for x in range(seed.width):
            result.append(Coordinates(x+origin_point.xpos, y+origin_point.ypos))

    logging.debug(f'Visible Units: {result}')
    logging.info(f'Generated Visible Units.\n')
    return result


def pick_value(seed, unit, picklist, saved_units):
    """
    Picks a value for a unit.
    :param pick_list:
    :return:
    """
    result = ''
    logging.debug('Picking value...')

    for _unit in saved_units:
        if unit.xpos == _unit.coordinates.xpos and unit.ypos == _unit.coordinates.ypos:
            logging.debug('Unit exists in saved Units...')
            result = _unit.value
            break

    else:
        logging.debug('Generating new unit...')
        result = random.Random(x=seed.seed + (unit.xpos + unit.ypos)).choice(picklist)

    logging.debug(f'Value: {result}')
    logging.info('Generated Value successfully.\n')
    return result


def generate_picklist(values):
    """
    Generates a picklist
    :param values:
    :return:
    """
    result = []
    logging.info('Generating picklist...')
    for value in values:
        for x in range(value.chance):
            result.append(value)

    logging.debug(f'Picklist: {result}')
    logging.info('Generated Picklist\n')
    return result


def generate_units(seed, visible_units, saved_units, picklist):
    """
    Creates units from a list of coordinates.
    :param values:
    :param visible_units:
    :return:
    """
    result = []
    logging.info('Generating units...')
    logging.info('Picking Values...')
    for unit in visible_units:
        result.append(Unit(pick_value(seed, unit, picklist, saved_units), unit))

    logging.info('Finished Picking Values...')

    logging.debug(f'Number of Units: {seed.width*seed.length}')
    logging.info('Generated all units\n')
    return result
