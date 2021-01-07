import math


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def dist(self, point: 'Point') -> float:
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
