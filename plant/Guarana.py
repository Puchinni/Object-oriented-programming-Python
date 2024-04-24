from Plant import Plant


class Guarana(Plant):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.initiative = 0
        self.strength = 0

    def Action(self, w):
        super().Action(w)
        if self._plantX != -1 and self._plantY != -1 and w.isEmptyCell(self._plantX, self._plantY):
            w.organism_setter(Guarana(self._plantX, self._plantY))
            w.setOrganismOnBoard(self._plantX, self._plantY, w.organism_del())
        self._plantX = -1
        self._plantY = -1

    def Collision(self, org):
        if self._strength < org.GetStrength():
            org.SetStrength(org.GetStrength() + 3)
            self.Died()

    def Draw(self):
        return "Guarana"

    def GetColor(self):
        return "cyan"
