from AlgoCiv.engine.gravity.grid.value import *
import datetime


class Coordinates:
    """
    Coordinates.
    """
    def __init__(self, x_position: int, y_position: int):
        self.xpos = x_position
        self.ypos = y_position

    def __repr__(self):
        return f"Coordinates(X-Position: {self.xpos}, Y-Position: {self.ypos})"


class Unit:
    """
    A single "cell" in a grid object.
    """
    def __init__(self, value: Value, coordinates: Coordinates):
        self.value = value
        self.coordinates = coordinates

    def __repr__(self):
        return f"Unit({self.value}, {self.coordinates}"

