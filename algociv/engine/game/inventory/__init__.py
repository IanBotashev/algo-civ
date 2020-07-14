from algociv.engine.game.inventory.errors import *


class Inventory:
    def __init__(self, slots: int):
        self.inventory = []
        self.slots = slots

    def append(self, item):
        if len(self.inventory) + 1 > self.slots:
            raise InventoryFull(f'Cannot add another item. Inventory capacity has been reached.')
        self.inventory.append(item)

    def remove(self, item):
        self.inventory.remove(item)
