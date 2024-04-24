from Animal import Animal


class Human(Animal):

    def __init__(self, x, y):
        super().__init__(x, y)
        self._initiative = 4
        self._baseStrength = self._strength = 5

    def SetX(self, x):
        self._x = x

    def SetY(self, y):
        self._y = y

    def GetX(self):
        return self._x

    def GetY(self):
        return self._y

    def Action(self, w):
        pass

    def Collision(self, org):
        if self._strength < org.GetStrength():
            self.Died()

    def activateAbility(self):
        if 10 > self._baseStrength >= 5:
            self._baseStrength += 1

    def disactivateAbility(self):
        if 10 >= self._baseStrength > 5:
            self._baseStrength -= 1

    def Draw(self):
        return "Human"

    def GetColor(self):
        return "magenta"

    def GetStrength2(self):
        return self._baseStrength

    def SetStrength2(self, baseStrength):
        self._baseStrength = baseStrength




