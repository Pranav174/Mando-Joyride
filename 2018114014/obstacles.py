from stuff import stuff
from colorama import Fore, Back
import random

class backgound_objects(stuff):
    def __init__(self):
        super().__init__()
        self._ux = -3
        self._minx = -100
        self._x = self._maxx

class bars(backgound_objects):
    def __init__(self):
        super().__init__()
        self._color = Fore.RED
        self._type = random.randint(1,3)
        self._y = random.randint(self._miny+8, self._maxy-10)
        if self._type == 1:
            self._shape = [
                    "/~\\",
                    "| |",
                    "| |",
                    "| |",
                    "| |",
                    "| |",
                    "| |",
                    "| |",
                    "| |",
                    "| |",
                    "\~/"
                ]
        elif self._type == 2:
            self._shape = [
                    "/~~~~~~~~~~~~~~~~~~~~~~\\",
                    "\~~~~~~~~~~~~~~~~~~~~~~/"
                ]
        else:
            self._shape = [
                    "         /~|",
                    "        / / ",
                    "       / /  ",
                    "      / /   ",
                    "     / /    ",
                    "    / /     ",
                    "   / /      ",
                    "  / /       ",
                    " / /        ",
                    "|~/         "
                ]
        self._height = len(self._shape)
        self._width = len(self._shape[0])


class coins(backgound_objects):
    def __init__(self):
        super().__init__()
        self._bgcolor = Back.LIGHTYELLOW_EX
        self._color = Fore.BLACK
        self._shape = [
            "/~\\",
            "|$|",
            "\_/"
        ]
        self._height = len(self._shape)
        self._width = len(self._shape[0])
        self._y = random.randint(self._miny+8, self._maxy-8)
        self._eaten = False
    
    def isEaten(self):
        return self._eaten

    def eat(self):
        self._eaten = True

class magnet(backgound_objects):
    def __init__(self):
        super().__init__()
        self._bgcolor = Back.LIGHTBLUE_EX
        self._color = Fore.RED
        self._shape = [
            "| |",
            "\_/"
        ]
        self._height = len(self._shape)
        self._width = len(self._shape[0])
        self._y = random.randint(self._miny+8, self._maxy-8)

    def getCenter(self):
        return self._x + 2, self._y + 1

class speedBoost(backgound_objects):
    def __init__(self):
        super().__init__()
        self._bgcolor = Back.LIGHTGREEN_EX
        self._color = Fore.MAGENTA
        self._shape = [
            " ** ",
            "*  *",
            " ** "
        ]
        self._height = len(self._shape)
        self._width = len(self._shape[0])
        self._y = random.randint(self._miny+8, self._maxy-8)

class clouds(backgound_objects):
    def __init__(self):
        super().__init__()
        self._shape = [['☁']]
        self._color = Fore.BLUE
        self._height = 1
        self._width = 1
        self._miny = 0
        self._y = random.randint(0,3)