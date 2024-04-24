from Plant import Plant


class WolfBerries(Plant):

    def __init__(self, x, y):
        super().__init__(x, y)
        self._strength = 99
        self._initiative = 0

    def Collision(self, org):
        if self._strength < org.GetStrength():
            self.Died()

    def Action(self, w):
        super().Action(w)
        if self._plantX != -1 and self._plantY != -1 and w.isEmptyCell(self._plantX, self._plantY):
            w.organism_setter(WolfBerries(self._plantX, self._plantY))
            w.setOrganismOnBoard(self._plantX, self._plantY, w.organism_del())
        self._plantX = -1
        self._plantY = -1

    def Draw(self):
        return "WolfBerries"

    def GetColor(self):
        return "brown"

