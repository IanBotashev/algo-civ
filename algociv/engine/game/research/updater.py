def update_structures(workers, buildings, traits):
    """
    Updates structures to the current research
    :param workers:
    :param buildings:
    :return:
    """
    update_workers(workers)
    update_buildings(buildings)


def check_module_effect(structure, trait):
    """
    Checks if a trait is being affected by a module.
    :param structure:
    :return:
    """
    for module in structure.__modules__.__modules__:
        if trait in module.__traits__:
            return True

    return False


def update_workers(workers, traits):
    """
    Keeps workers up-to-date with research
    :param workers:
    :return:
    """
    map = [
        ''
    ]
    for worker in workers:



def update_buildings(buildings):
    """
    Keeps buildings up-to-date with research
    :param buildings:
    :return:
    """
    pass
