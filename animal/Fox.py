from Animal import Animal


class Fox(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._step_y = [-1, -1, -1, 0, 0, 1, 1, 1]
        self._step_x = [-1, 0, 1, -1, 1, -1, 0, 1]
        self._initiative = 7
        self._strength = 3

    def Action(self, w):
        stepCount = 0
        for i in range(8):
            if not w.isCellExists(self._x + self._step_x[i], self._y + self._step_y[i]):
                stepCount += 1

        while stepCount < 8:
            x_ = self._GetRandomX(w)
            y_ = self._GetRandomY(w)
            if w.isCellExists(x_, y_):
                if w.isEmptyCell(x_, y_):
                    self._x = x_
                    self._y = y_
                    return
                else:
                    org = w.GetOrganismByPosition(x_, y_)
                    if org.GetStrength() >= self.GetStrength():
                        return
                    org.Collision(self)
                    return

    def Collision(self, org):
        if isinstance(org, Fox):
            for i in range(8):
                x_ = self._x + self._step_x[i]
                y_ = self._y + self._step_y[i]
                if self._world.isCellExists(x_, y_) and self._world.isEmptyCell(x_, y_):
                    if isinstance(self, Fox):
                        new_animal = Fox(x_, y_)
                        new_animal.SetWorld(self._world)
                        self._world.organism_setter(new_animal)
                        return

            for i in range(8):
                x_ = org.GetX() + self._step_x[i]
                y_ = org.GetY() + self._step_y[i]
                if self._world.isCellExists(x_, y_) and self._world.isEmptyCell(x_, y_):
                    if isinstance(org, Fox):
                        new_animal = Fox(x_, y_)
                        new_animal.SetWorld(self._world)
                        self._world.organism_setter(new_animal)
                        return
        else:
            if self._strength < org.GetStrength():
                self.Died()

    def Draw(self):
        return "Fox"

    def GetColor(self):
        return "blue"
