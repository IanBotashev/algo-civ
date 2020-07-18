def is_mineable(material, mineables):
    """
    Checks if a material is mineable
    :param material:
    :param mineables:
    :return:
    """
    if material in mineables:
        return True

    # Else
    return False


def check_required_materials(required_mats, owned_mats):
    """
    Checks if the user has the required materials to craft something.
    :param required_mats:
    :param owned_mats:
    :return:
    """
    check = all(item in owned_mats for item in required_mats)
    return check


def is_craftable(item, craftables):
    """
    Checks if an item is craftable
    :param item:
    :param craftables:
    :return:
    """
    if item in craftables:
        return True
    # Else
    return False
