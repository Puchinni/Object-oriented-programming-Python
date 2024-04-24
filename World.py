from Animal import Animal
from Plant import Plant


class World:
    def __init__(self, row, col, organisms=None, human=None):

        self._row = row
        self._col = col
        self._turn = 0
        self._stepCount = 0
        self._human = human
        if organisms:
            self._organisms = organisms
        self._organisms = []
        self._organismsBoard = [[None for _ in range(col)] for _ in range(row)]

    def human_setter(self, human):
        self._human = human
        self._organisms.append(human)

    def organisms_getter(self):
        return self._organisms

    def organism_setter(self, organism):
        self._organisms.append(organism)

    def organism_del(self):
        return self._organisms[-1]

    def GetRow(self):
        return self._row

    def GetCol(self):
        return self._col

    def ClearBoard(self):
        for i in range(self._row):
            for j in range(self._col):
                self._organismsBoard[i][j] = None

    def GetOrganismByPosition(self, x, y):
        for org in self._organisms:
            if org.GetX() == x and org.GetY() == y:
                return org
        return None

    def setOrganismOnBoard(self, x, y, org):
        self._organismsBoard[y][x] = org

    def isEmptyCell(self, x, y):
        return self._organismsBoard[y][x] is None

    def isCellExists(self, x, y):
        return not (x < 0 or x >= self._col or y < 0 or y >= self._row)

    def MoveHuman(self, dx, dy):
        newX = self._human.GetX() + dx
        newY = self._human.GetY() + dy
        if newX < 0 or newX >= self._col or newY < 0 or newY >= self._row:
            return
        self._human.SetX(newX)
        self._human.SetY(newY)

    def SetStepCount(self, stepCount):
        self._stepCount = stepCount


    def ExecuteTure(self):
        self._organisms.sort(key=lambda o: (o.GetInitiative(), o.GetAge()), reverse=True)
        self.ClearBoard()
        self._stepCount += 1
        if self._stepCount == 10:
            self._stepCount = 0
        print("Turn: ", self._turn)
        self._turn += 1
        currentSize = len(self._organisms)
        for i in range(currentSize):
            self._organisms[i].Action(self)
            if isinstance(self._organisms[i], Animal) \
                    and self._organismsBoard[self._organisms[i].GetY()][self._organisms[i].GetX()] is not None:
                self._organisms[i].Collision(self._organismsBoard[self._organisms[i].GetY()][self._organisms[i].GetX()])
                self._organismsBoard[self._organisms[i].GetY()][self._organisms[i].GetX()].Collision(self._organisms[i])
                print(self._organisms[i].Draw(), "x",
                      self._organismsBoard[self._organisms[i].GetY()][self._organisms[i].GetX()].Draw())
            if isinstance(self._organisms[i], Plant) \
                    and self._organismsBoard[self._organisms[i].GetY()][self._organisms[i].GetX()] is not None:
                self._organisms[i].Collision(self._organismsBoard[self._organisms[i].GetY()][self._organisms[i].GetX()])
                self._organismsBoard[self._organisms[i].GetY()][self._organisms[i].GetX()].Collision(self._organisms[i])
                print(self._organisms[i].Draw(), "x",
                      self._organismsBoard[self._organisms[i].GetY()][self._organisms[i].GetX()].Draw())
            self._organismsBoard[self._organisms[i].GetY()][self._organisms[i].GetX()] = self._organisms[i]

        for i in range(currentSize, len(self._organisms)):
            if self._organismsBoard[self._organisms[i].GetY()][self._organisms[i].GetX()] is not None:
                other = self._organismsBoard[self._organisms[i].GetY()][self._organisms[i].GetX()]
                self._organisms[i].Collision(other)
                other.Collision(self._organisms[i])

        i = 0
        while i < len(self._organisms):
            if self._organisms[i].IsDied():
                self._organismsBoard[self._organisms[i].GetY()][self._organisms[i].GetX()] = None
                print(self._organisms[i].Draw(), "-> is died!")
                self._organisms.pop(i)
            else:
                i += 1

        print("H [{}; {}]".format(self._organisms[0].GetX(), self._organisms[0].GetY()))
        print("Organism Count:", len(self._organisms))

