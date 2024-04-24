from Plant import Plant


class Hogweed(Plant):

    def __init__(self, x, y):
        super().__init__(x, y)
        self._step_y = [-1, -1, -1, 0, 0, 1, 1, 1]
        self._step_x = [-1, 0, 1, -1, 1, -1, 0, 1]
        self._strength = 99
        self._initiative = 0

    def Action(self, w):
        super().Action(w)
        if self._plantX != -1 and self._plantY != -1 and w.isEmptyCell(self._plantX, self._plantY):
            w.organism_setter(Hogweed(self._plantX, self._plantY))
            w.setOrganismOnBoard(self._plantX, self._plantY, w.organism_del())
        self._plantX = -1
        self._plantY = -1
        for i in range(8):
            x_ = self._x + self._step_x[i]
            y_ = self._y + self._step_y[i]
            if w.isCellExists(x_, y_) and not w.isEmptyCell(x_, y_):
                other = w.GetOrganismByPosition(x_, y_)
                if not isinstance(other, Hogweed):
                    if other.__class__.__name__ != 'CyberSheep':
                        other.Died()
                        return

    def Collision(self, org):
        if not isinstance(org, Hogweed):
            if org.__class__.__name__ != 'CyberSheep':
                org.Died()

    def Draw(self):
        return "Hogweed"

    def GetColor(self):
        return "dark gray"
