from algociv.engine.gravity.grid.value import *
from math import sqrt


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


def find_distance(point1: Coordinates, point2: Coordinates):
    """
    Finds the distance between two points.
    :param point1:
    :param point2:
    :return:
    """
    x_distance = pow(point1.xpos - point2.xpos, 2)
    y_distance = pow(point1.ypos - point2.ypos, 2)
    distance = round(sqrt(x_distance + y_distance))

    return distance


class Dimensions:
    def __init__(self, y_dimension, x_dimension):
        self.y = y_dimension
        self.x = x_dimension

    def __repr__(self):
        return f"<Dimensions(x: {self.x}, y: {self.y})>"
