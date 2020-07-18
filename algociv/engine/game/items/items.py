from algociv.engine.game.items.materials import *


class Item:
    name = None
    description = None
    craft = []


class SampleItem:
    name = "Sample Item"
    description = "A test item. Not supposed to be in-game"
    craft = [Dirt]
