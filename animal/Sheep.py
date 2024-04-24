from Animal import Animal


class Sheep(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._strength = 4
        self._initiative = 4

    def Action(self, w):
        super().Action(w)

    def Collision(self, org):
        if isinstance(org, Sheep):
            for i in range(8):
                x_ = self._x + self._step_x[i]
                y_ = self._y + self._step_y[i]
                if self._world.isCellExists(x_, y_) and self._world.isEmptyCell(x_, y_):
                    if isinstance(self, Sheep):
                        new_animal = Sheep(x_, y_)
                        new_animal.SetWorld(self._world)
                        self._world.organism_setter(new_animal)
                        return

            for i in range(8):
                x_ = org.GetX() + self._step_x[i]
                y_ = org.GetY() + self._step_y[i]
                if self._world.isCellExists(x_, y_) and self._world.isEmptyCell(x_, y_):
                    if isinstance(org, Sheep):
                        new_animal = Sheep(x_, y_)
                        new_animal.SetWorld(self._world)
                        self._world.organism_setter(new_animal)
                        return
        else:
            if self._strength < org.GetStrength():
                self.Died()

    def Draw(self):
        return "Sheep"

    def GetColor(self):
        return "yellow"
