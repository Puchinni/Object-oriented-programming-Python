from abc import ABC, abstractmethod
import random
from Organism import Organism


class Animal(Organism, ABC):
    def __init__(self, x, y):
        super().__init__()
        self._step_y = [-1, -1, -1, 0, 0, 1, 1, 1]
        self._step_x = [-1, 0, 1, -1, 1, -1, 0, 1]
        self._x = x
        self._y = y
        self._world = None

    def SetWorld(self, w):
        self._world = w

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
        self._x = self._GetRandomX(w)
        self._y = self._GetRandomY(w)



