class Item:
    def __repr__(self):
        return_string = f"<Item(name: {self.__class__.__name__})>"
        return return_string


class Coal(Item):
    pass
