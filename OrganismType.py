

class OrganismType:
    EMPTY = ' '
    Fox = 'F'
    Guarana = 'G'
    Grass = '#'
    Hogweed = 'h'
    Human = 'H'
    Sonchus = 'K'
    CyberSheep = 'C'
    Sheep = 'S'
    Turtle = 'T'
    Wolf = 'W'
    WolfBerries = '&'
    Antelope = 'A'

    @staticmethod
    def get_symbol(type):
        if type == OrganismType.EMPTY:
            return ' '
        elif type == OrganismType.Fox:
            return 'F'
        elif type == OrganismType.CyberSheep:
            return 'C'
        elif type == OrganismType.Guarana:
            return 'G'
        elif type == OrganismType.Grass:
            return '#'
        elif type == OrganismType.Hogweed:
            return 'h'
        elif type == OrganismType.Human:
            return 'H'
        elif type == OrganismType.Sonchus:
            return 'K'
        elif type == OrganismType.Sheep:
            return 'S'
        elif type == OrganismType.Turtle:
            return 'T'
        elif type == OrganismType.Wolf:
            return 'W'
        elif type == OrganismType.WolfBerries:
            return '&'
        elif type == OrganismType.Antelope:
            return 'A'
        else:
            raise ValueError("Unknown organism type: " + type)
