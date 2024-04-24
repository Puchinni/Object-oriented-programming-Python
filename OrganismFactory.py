from animal.Antelope import Antelope
from animal.CyberSheep import CyberSheep
from animal.Fox import Fox
from animal.Sheep import Sheep
from plant.Grass import Grass
from plant.Hogweed import Hogweed
from plant.Guarana import Guarana
from plant.Sonchus import Sonchus
from plant.WolfBerries import WolfBerries
from animal.Turtle import Turtle
from animal.Wolf import Wolf
from animal.Human import Human
from OrganismType import OrganismType


class OrganismFactory:
    @staticmethod
    def create(type, x, y):
        if type == OrganismType.EMPTY:
            return None
        elif type == OrganismType.Fox:
            return Fox(x, y)
        elif type == OrganismType.CyberSheep:
            return CyberSheep(x, y)
        elif type == OrganismType.Guarana:
            return Guarana(x, y)
        elif type == OrganismType.Grass:
            return Grass(x, y)
        elif type == OrganismType.Human:
            return Human(x, y)
        elif type == OrganismType.Hogweed:
            return Hogweed(x, y)
        elif type == OrganismType.Sonchus:
            return Sonchus(x, y)
        elif type == OrganismType.Sheep:
            return Sheep(x, y)
        elif type == OrganismType.Turtle:
            return Turtle(x, y)
        elif type == OrganismType.Wolf:
            return Wolf(x, y)
        elif type == OrganismType.WolfBerries:
            return WolfBerries(x, y)
        elif type == OrganismType.Antelope:
            return Antelope(x, y)
        else:
            raise RuntimeError("Unknown organism type: " + type)



