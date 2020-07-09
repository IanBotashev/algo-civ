class Inventory:
    def __init__(self):
        self.inventory = []

    def append(self, item):
        self.inventory.append(item)

    def remove(self, item):
        self.inventory.remove(item)
