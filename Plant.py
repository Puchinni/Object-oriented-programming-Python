from abc import ABC, abstractmethod
import random
from Organism import Organism


class Plant(Organism, ABC):
    def __init__(self, x, y):
        super().__init__()
        self._probability = 12.0
        self._plantX = -1
        self._plantY = -1
        self._x = x
        self._y = y
        self._world = None

    def _GetRandomX(self, w):
        while True:
            x = random.randint(-1, 1)
            result_x = self._x + x
            if 0 <= result_x < w.GetCol():
                return result_x

    def _GetRandomY(self, w):
        while True:
            y = random.randint(-1, 1)
            result_y = self._y + y
            if 0 <= result_y < w.GetCol():
                return result_y

    @abstractmethod
    def Action(self, w):
        self._world = w
        if random.randint(0, int(self._probability)) == 0:
            self._plantX = self._GetRandomX(w)
            self._plantY = self._GetRandomY(w)
            self._probability += 0.5
