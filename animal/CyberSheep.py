from Animal import Animal
from plant.Hogweed import Hogweed
from animal.Sheep import Sheep


class CyberSheep(Animal):

    def __init__(self, x, y):
        super().__init__(x, y)
        self._initiative = 4
        self._strength = 11

    def Collision(self, org):
        if isinstance(org, Hogweed):
            org.Died()
        elif self._strength < org.GetStrength():
            self.Died()

    def Action(self, w):
        hogweed_present = False
        for organism in w.organisms_getter():
            if isinstance(organism, Hogweed):
                hogweed_present = True
                break

        if hogweed_present:
            self.find_hogweed(w)
        else:
            self.turn_into_sheep()


    def Draw(self):
        return "CyberSheep"

    def GetColor(self):
        return "Pink"

    def find_hogweed(self, world):
        hogweed_coords = []
        for i in range(world.GetRow()):
            for j in range(world.GetCol()):
                organism = world.GetOrganismByPosition(j, i)
                if isinstance(organism, Hogweed):
                    hogweed_coords.append((j, i))

        if hogweed_coords:
            self.move_towards_hogweed(hogweed_coords)

    def move_towards_hogweed(self, hogweed_coords):
        min_distance = 999999
        target_coords = None
        for coord in hogweed_coords:
            distance = abs(coord[0] - self.GetX()) + abs(coord[1] - self.GetY())
            if distance < min_distance:
                min_distance = distance
                target_coords = coord

        if target_coords:
            dx = target_coords[0] - self.GetX()
            dy = target_coords[1] - self.GetY()
            if dx < 0:
                self.SetX(self.GetX() - 1)

            elif dx > 0:
                self.SetX(self.GetX() + 1)

            elif dy < 0:
                self.SetY(self.GetY() - 1)

            elif dy > 0:
                self.SetY(self.GetY() + 1)

    def turn_into_sheep(self):
        self.__class__ = Sheep
        Sheep.SetStrength(self, 4)
        Sheep.SetInitiative(self, 4)

