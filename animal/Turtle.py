from Animal import Animal
import random


class Turtle(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.initiative = 1
        self.strength = 2

    def Action(self, w):
        if random.randint(0, 100) > 75:
            super().Action(w)

    def Collision(self, org):
        if isinstance(org, Turtle):
            for i in range(8):
                x_ = self._x + self._step_x[i]
                y_ = self._y + self._step_y[i]
                if self._world.isCellExists(x_, y_) and self._world.isEmptyCell(x_, y_):
                    if isinstance(self, Turtle):
                        new_animal = Turtle(x_, y_)
                        new_animal.SetWorld(self._world)
                        self._world.organism_setter(new_animal)
                        return

            for i in range(8):
                x_ = org.GetX() + self._step_x[i]
                y_ = org.GetY() + self._step_y[i]
                if self._world.isCellExists(x_, y_) and self._world.isEmptyCell(x_, y_):
                    if isinstance(org, Turtle):
                        new_animal = Turtle(x_, y_)
                        new_animal.SetWorld(self._world)
                        self._world.organism_setter(new_animal)
                        return
        else:
            if 5 > org.GetStrength():
                pass
            else:
                if org.GetStrength() >= 5 and (self._strength < org.GetStrength()):
                    self.Died()

    def Draw(self):
        return "Turtle"

    def GetColor(self):
        return "orange"
