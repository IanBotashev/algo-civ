from algociv.engine.gravity.grid.assets import *
from algociv.engine.gravity.grid.value import *
import random
import logging
from math import sqrt


"""
This is the system responsible for generating the grids.
"""


def generation_algorithm(seed, unit):
    """
    The generation algorithm.
    :param seed:
    :return:
    """
    seedrandom = random.Random(x=seed.seed + ((unit.xpos + unit.ypos)*100))

    tempnum = seedrandom.randint(seed.start, seed.end)

    defnum = seedrandom.randint(tempnum - seed.start, seed.end)

    return defnum


def generate_visible_units(center_point, dimensions):
    """
    Generates a list of all visible units.
    It does not return a list of Unit building, but coordinate building.
    :param center_point:
    :param width:
    :param height:
    :return:
    """
    result = []
    origin_point = Coordinates(center_point.xpos-1, center_point.ypos-1)
    logging.info('Generating visible units...')

    for y in range(dimensions.x):
        for x in range(dimensions.y):
            result.append(Coordinates(x+origin_point.xpos, y+origin_point.ypos))

    logging.debug(f'Visible Units: {result}')
    logging.info(f'Generated Visible Units.\n')
    return result


def generate_value(seed, unit):
    """
    generates the value needed.
    :param seed:
    :return:
    """
    defnum = generation_algorithm(seed, unit)

    for value in seed.values:
        for chancenum in value.chance:
            if defnum == chancenum:
                return value

    return seed.default


def pick_value(seed, unit, saved_units):
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
        result = generate_value(seed, unit)

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


def generate_units(seed, visible_units, saved_units, dimensions):
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
        result.append(Unit(pick_value(seed, unit, saved_units), unit))

    logging.info('Finished Picking Values...')

    logging.debug(f'Number of Units: {dimensions.x*dimensions.y}')
    logging.info('Generated all units\n')
    return result
