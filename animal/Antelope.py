from Animal import Animal
import random


class Antelope(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._initiative = 4
        self._strength = 4

    def Action(self, w):
        super().Action(w)
        super().Action(w)

    def Collision(self, org):
        if isinstance(org, Antelope):
            for i in range(8):
                x_ = self._x + self._step_x[i]
                y_ = self._y + self._step_y[i]
                if self._world.isCellExists(x_, y_) and self._world.isEmptyCell(x_, y_):
                    if isinstance(self, Antelope):
                        new_animal = Antelope(x_, y_)
                        new_animal.SetWorld(self._world)
                        self._world.organism_setter(new_animal)
                        return

            for i in range(8):
                x_ = org.GetX() + self._step_x[i]
                y_ = org.GetY() + self._step_y[i]
                if self._world.isCellExists(x_, y_) and self._world.isEmptyCell(x_, y_):
                    if isinstance(org, Antelope):
                        new_animal = Antelope(x_, y_)
                        new_animal.SetWorld(self._world)
                        self._world.organism_setter(new_animal)
                        return

        if random.randint(0, 99) > 50:
            self.Action(self._world)
            self.Action(self._world)
            return
        if self._strength < org.GetStrength():
            self.Died()

    def Draw(self):
        return "Antelope"

    def GetColor(self):
        return "black"
