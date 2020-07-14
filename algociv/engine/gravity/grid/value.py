class Value:
    """
    This is an individual cell, but it's the content
    """
    def __init__(self, name, chance: list, **kwargs):
        self.name = name
        self.chance = chance
        self.kwargs = kwargs

    def format_kwargs(self):
        """
        Formats kwargs into a string
        :return:
        """
        result = ""
        for kwarg in self.kwargs:
            result += ', '
            result += f"{kwarg}: '{self.kwargs[kwarg]}'"

        return result

    def __repr__(self):
        return f"Value(name: {self.name}{self.format_kwargs()})"


def get_values_defnum(values, defnum):
    """
    Gets value in a list that has a specific defining number, and if it does, return it.
    :param values:
    :param defnum:
    :return:
    """
    for value in values:
        for _defnum in value.defnums:
            if _defnum == defnum:
                return value

    return False
