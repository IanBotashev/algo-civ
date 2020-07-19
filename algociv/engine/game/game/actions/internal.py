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
