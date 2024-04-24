from Plant import Plant


class Grass(Plant):

    def __init__(self, x, y):
        super().__init__(x, y)
        self._strength = 0
        self._initiative = 0

    def Collision(self, org):
        if self._strength < org.GetStrength():
            self.Died()

    def Action(self, w):
        super().Action(w)
        if self._plantX != -1 and self._plantY != -1 and w.isEmptyCell(self._plantX, self._plantY):
            w.organism_setter(Grass(self._plantX, self._plantY))
            w.setOrganismOnBoard(self._plantX, self._plantY, w.organism_del())
        self._plantX = -1
        self._plantY = -1

    def Draw(self):
        return "Grass"

    def GetColor(self):
        return "green"

