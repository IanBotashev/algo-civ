from algociv.engine.gravity.grid.assets import *
import logging
from noise import snoise2


# This is the system responsible for generating the grids.


def generate_visible_units(center_point, dimensions):
    """
    Generates a list of all visible units.
    It does not return a list of Unit building, but coordinate building.
    :param center_point:
    :param dimensions:
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


def generation_algorithm(seed, unit):
    """
    Uses simplex noise to generate a value.
    :param seed:
    :param unit:
    :return:
    """
    point = snoise2(unit.xpos/seed.scale, unit.ypos/seed.scale,
                    octaves=seed.octaves,
                    persistence=seed.persistence,
                    lacunarity=seed.lacunarity,
                    repeatx=1024,
                    repeaty=1024,
                    base=seed.seed)
    logging.debug(f"New Simplex Value: {point}")
    return point


def generate_value(seed, unit):
    """
    Gets a simplex noise value between -1 and 1, and then returns a value.
    :param seed:
    :param unit:
    :return:
    """
    int_value = generation_algorithm(seed, unit)

    for value in seed.values:
        if value.chance[0] <= int_value <= value.chance[1]:
            return value

    return seed.default


def pick_value(unit, grid):
    """
    Picks a value
    :param unit:
    :param grid:
    :return:
    """
    logging.debug('Picking value...')

    if (unit.xpos, unit.ypos) in grid.saved_units:
        logging.debug('Grabbing unit from saved units...')
        result = grid.saved_units[(unit.xpos, unit.ypos)]

    else:
        logging.debug('Generating new unit...')
        result = generate_value(grid.seed, unit)
        grid.update_saved_units(Unit(result, unit))

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


def generate_units(visible_units, grid, dimensions):
    """
    Creates units from a list of coordinates.
    :param visible_units:
    :param grid:
    :param dimensions:
    :return:
    """
    result = []
    logging.info('Generating units...')
    logging.info('Picking Values...')
    for unit in visible_units:
        result.append(Unit(pick_value(unit, grid), unit))

    logging.info('Finished Picking Values...')

    logging.debug(f'Number of Units: {dimensions.x*dimensions.y}')
    logging.info('Generated all units\n')
    return result
