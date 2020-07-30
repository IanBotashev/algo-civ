def update_structures(workers, buildings):
    """
    Updates structures to the current research
    :param workers:
    :param buildings:
    :param traits:
    :return:
    """
    structures = workers + buildings

    for structure in structures:
        structure.update()
