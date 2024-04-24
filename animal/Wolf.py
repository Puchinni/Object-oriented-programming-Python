from Animal import Animal


class Wolf(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._strength = 9
        self._initiative = 5

    def Action(self, w):
        super().Action(w)

    def Collision(self, org):
        if isinstance(org, Wolf):
            for i in range(8):
                x_ = self._x + self._step_x[i]
                y_ = self._y + self._step_y[i]
                if self._world.isCellExists(x_, y_) and self._world.isEmptyCell(x_, y_):
                    if isinstance(self, Wolf):
                        new_animal = Wolf(x_, y_)
                        new_animal.SetWorld(self._world)
                        self._world.organism_setter(new_animal)
                        return

            for i in range(8):
                x_ = org.GetX() + self._step_x[i]
                y_ = org.GetY() + self._step_y[i]
                if self._world.isCellExists(x_, y_) and self._world.isEmptyCell(x_, y_):
                    if isinstance(org, Wolf):
                        new_animal = Wolf(x_, y_)
                        new_animal.SetWorld(self._world)
                        self._world.organism_setter(new_animal)
                        return
        else:
            if self._strength < org.GetStrength():
                self.Died()

    def Draw(self):
        return "Wolf"

    def GetColor(self):
        return "red"
