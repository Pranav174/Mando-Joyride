from stuff import stuff
from stuff import Fore,Back
class bullets(stuff):
    def __init__(self, x, y):
        super().__init__()
        self._x = x
        self._y = y
        self._minx = -20
        self._maxx = 300

class blasters(bullets):
    def __init__(self, x, y):
        super().__init__(x,y)
        self._ux = 5
        self._shape = ['=====']
        self._width = 5
        self._color = Fore.BLACK
        self._bgcolor = Back.LIGHTWHITE_EX

class iceBalls(bullets):
    def __init__(self,x,y):
        super().__init__(x,y)
        self._shape = [
            "ooo",
            "ooo",
            "ooo"
        ]
        self._ux = -5
        self._uy = -1
        self._ay = 0.1
        self._width = len(self._shape[0])
        self._height = len(self._shape)
        self._color = Fore.WHITE
        self._bgcolor = Fore.BLUE
