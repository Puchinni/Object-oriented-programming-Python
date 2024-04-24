from abc import ABC, abstractmethod


class Organism(ABC):
    def __init__(self):
        self._strength = 0
        self._initiative = 0
        self._age = 0
        self._x = -1
        self._y = -1
        self.isDied = False

    @abstractmethod
    def Action(self, w):
        pass

    @abstractmethod
    def Collision(self, org):
        pass

    @abstractmethod
    def Draw(self):
        pass

    def SetX(self, x):
        self._x = x

    def SetY(self, y):
        self._y = y

    def GetX(self):
        return self._x

    def GetY(self):
        return self._y

    def GetStrength(self):
        return self._strength

    def SetStrength(self, strength):
        self._strength = strength

    def GetInitiative(self):
        return self._initiative

    def SetInitiative(self, initiative):
        self._initiative = initiative

    def GetAge(self):
        return self._age

    def SetAge(self, age):
        self._age = age

    def Died(self):
        self.isDied = True

    def IsDied(self):
        return self.isDied
