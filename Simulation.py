import tkinter
import tkinter as tk
from tkinter import filedialog
import tkinter.simpledialog
from OrganismFactory import OrganismFactory
from OrganismType import OrganismType
from World import World
from animal.Antelope import Antelope
from animal.Fox import Fox
from animal.Sheep import Sheep
from plant.Grass import Grass
from plant.Hogweed import Hogweed
from plant.Guarana import Guarana
from plant.Sonchus import Sonchus
from plant.WolfBerries import WolfBerries
from animal.Human import Human
from animal.Turtle import Turtle
from animal.Wolf import Wolf
from animal.CyberSheep import CyberSheep






def show_hint_window():
    hint_window = tk.Toplevel(window)
    hint_window.title("Hint")
    message = """
    Black: Antelope
    Pink: CyberSheep
    Blue: Fox
    Green: Grass
    Cyan: Guarana
    Dark Gray: Hogweed
    Magenta: Human
    Purple: Sonchus
    Yellow: Sheep
    Orange: Turtle
    Red: Wolf
    Brown: WolfBerries"""
    hint_window.geometry("300x200")
    hint_label = tk.Label(hint_window, text=message, justify=tk.LEFT)
    hint_label.pack()


def save(fName):
    try:
        with open(fName, "w") as writer:
            existingOrganisms = [o for o in world._organisms if not isinstance(o, Human) and 0 <= o.GetX() < world._row and 0 <= o.GetY() < world._col]
            writer.write(f"{world._row} {world._col}\n")
            writer.write(f"{human.GetX()} {human.GetY()} {human.GetStrength2()} {world._stepCount}\n")
            writer.write(f"{len(existingOrganisms)}\n")
            for o in existingOrganisms:
                writer.write(f"{o.__class__.__name__} {o.GetX()} {o.GetY()}\n")
    except IOError as ex:
        raise RuntimeError(ex)


def restore(fName):
    try:
        with open(fName, "r") as fin:
            for i in range(world._row):
                for j in range(world._col):
                    world._organismsBoard[i][j] = None
            world._organisms.clear()
            tokens = fin.readline().split(" ")
            row = int(tokens[0])
            col = int(tokens[1])
            humanData = fin.readline().split(" ")
            human._x = int(humanData[0])
            human._y = int(humanData[1])
            human.SetStrength2(int(humanData[2]))
            world.SetStepCount(int(humanData[3]))
            organismsBoard = [[None for _ in range(col)] for _ in range(row)]
            numOrganisms = int(fin.readline())
            for _ in range(numOrganisms):
                organismData = fin.readline().split(" ")
                organismType = organismData[0]
                x = int(organismData[1])
                y = int(organismData[2])
                organismTypeEnum = getattr(OrganismType, organismType)
                o = OrganismFactory.create(organismTypeEnum, x, y)
                organismsBoard[y][x] = o
                world.organism_setter(o)
                world.human_setter(human)

            draw_organisms()
    except IOError as ex:
        raise RuntimeError(ex)



def save_to_file():
    fName = filedialog.asksaveasfilename(defaultextension=".txt")
    if fName:
        try:
            save(fName)
            print("Complete! Press any key...")
        except RuntimeError as ex:
            print(f"Error saving file: {ex}")


def load_from_file():
    fName = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if fName:
        try:
            restore(fName)
            print("Complete! Press any key...")
        except RuntimeError as ex:
            print(f"Error loading file: {ex}")

def on_mouse_click(event):
    x = event.x
    y = event.y
    x = x // 25
    y = ((y - 40) // 25) + 2
    print(x, y)
    insert(x, y)

def insert(x, y):
    if 0 <= x < world._col and 0 <= y < world._row:
        print(x, y)
        if world.isEmptyCell(x, y):
            names = [
                "Sheep",
                "Antelope",
                "Fox",
                "Turtle",
                "Wolf",
                "Grass",
                "Guarana",
                "Hogweed",
                "Sonchus",
                "WolfBerries"
            ]
            selected_name = tkinter.simpledialog.askstring(
                "Add organism",
                "Select an organism:",
                initialvalue=names[0],
                parent=window
            )
            if selected_name:
                new_org = None
                if selected_name == "Sheep":
                    new_org = Sheep(x, y)
                elif selected_name == "Antelope":
                    new_org = Antelope(x, y)
                elif selected_name == "Fox":
                    new_org = Fox(x, y)
                elif selected_name == "Turtle":
                    new_org = Turtle(x, y)
                elif selected_name == "CyberSheep":
                    new_org = CyberSheep(x, y)
                elif selected_name == "Wolf":
                    new_org = Wolf(x, y)
                elif selected_name == "Grass":
                    new_org = Grass(x, y)
                elif selected_name == "Guarana":
                    new_org = Guarana(x, y)
                elif selected_name == "Hogweed":
                    new_org = Hogweed(x, y)
                elif selected_name == "Sonchus":
                    new_org = Sonchus(x, y)
                elif selected_name == "WolfBerries":
                    new_org = WolfBerries(x, y)

                if new_org:
                    world.organism_setter(new_org)
                    world.setOrganismOnBoard(x, y, new_org)
                    draw_organisms()

def on_key_press(event):
    key_code = event.keysym
    if key_code == "Up":
        world.MoveHuman(0, -1)
        world.ExecuteTure()
    elif key_code == "Down":
        world.MoveHuman(0, 1)
        world.ExecuteTure()
    elif key_code == "Left":
        world.MoveHuman(-1, 0)
        world.ExecuteTure()
    elif key_code == "Right":
        world.MoveHuman(1, 0)
        world.ExecuteTure()
    elif key_code == "u":
        if world._stepCount >= 0 and world._stepCount < 5:
            human.activateAbility()
            print("Ability is activated. Strength: " + str(human.GetStrength2()))
        elif world._stepCount >= 5 and world._stepCount < 10:
            human.disactivateAbility()
            print("Cooldown. Strength: " + str(human.GetStrength2()))
    draw_organisms()


def draw_organisms():
    canvas.delete("all")

    for organism in world.organisms_getter():
        draw_organism(organism)


def draw_organism(organism):
    size = 25
    x = organism.GetX()  * size
    y = organism.GetY() * size
    canvas.create_rectangle(x,y,x+size,y+size,fill=organism.GetColor(),outline='')



def add_hood(window):
    button_container = tk.Frame(window)
    button_container.pack(pady=10, fill=tk.BOTH)

    button2 = tk.Button(button_container, text="Hint",
                        command=show_hint_window)
    button2.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

    button_container2 = tk.Frame(window)
    button_container2.pack(pady=10, fill=tk.BOTH)

    button3 = tk.Button(button_container2, text="Save to file",
                        command=save_to_file)
    button3.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

    button4 = tk.Button(button_container2, text="Load from file",
                        command=load_from_file)
    button4.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

    window.bind()
    window.bind("<Button-3>", on_mouse_click)
    window.bind("<Key>", on_key_press)


x = int(input("Rows: "))
y = int(input("Cols: "))
size = [20, 20]
world = World(size[0], size[1])
human = Human(19, 0)
grass = Grass(0, 0)
hogweed = Hogweed(3, 3)
hogweed2 = Hogweed(15, 5)
fox = Fox(13, 14)
antelope = Antelope(7, 7)
sheep = Sheep(0, 18)
turtle = Turtle(19, 0)
wolf = Wolf(0, 10)
guarana = Guarana(3, 18)
sonchus = Sonchus(18, 3)
wolfberries = WolfBerries(10, 19)
cyber_sheep = CyberSheep(16, 18)
world.human_setter(human)
world.organism_setter(grass)
#world.organism_setter(hogweed)
world.organism_setter(hogweed2)
world.organism_setter(antelope)
world.organism_setter(fox)
world.organism_setter(sheep)
world.organism_setter(turtle)
world.organism_setter(wolf)
world.organism_setter(wolfberries)
world.organism_setter(sonchus)
world.organism_setter(guarana)
world.organism_setter(cyber_sheep)

window = tk.Tk()
window.title("Aliaksei Yashynski 196691")
size[0] *= 25
size[1] = size[1] * 25 + 100
size_str = [str(x) for x in size]
window.geometry("x".join(size_str))

canvas = tk.Canvas(window,width=size[0],height=size[1]-100)
canvas.pack()

add_hood(window)

draw_organisms()

window.mainloop()
