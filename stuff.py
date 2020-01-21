from colorama import Fore,Back

class stuff:
    def __init__(self):
        self._color = Fore.WHITE
        self._bgcolor = Back.BLACK
        self._width = 1
        self._height = 1
        self._x = 8
        self._y = 8
        self._ux = 0
        self._uy = 0
        self._ax = 0
        self._ay = 0
        self._minx = 0
        self._maxx = 200
        self._miny = 5
        self._maxy = 50
        self._shape = [[' ']]

    def getPOS(self,speedBoost):
        # Update POS
        if speedBoost:
            self._x += (self._ux + 0.5 * self._ax)*1.4
            self._y += (self._uy + 0.5 * self._ay)*1.4
        else:
            self._x += self._ux + 0.5 * self._ax
            self._y += self._uy + 0.5 * self._ay
            
        self._x = max(self._x, self._minx)
        self._x = min(self._x, self._maxx)
        self._y = max(self._y, self._miny)
        self._y = min(self._y, self._maxy)
        if self._y == self._miny and self._uy<0:
            self._uy = 0
        if self._y == self._maxy and self._uy>0:
            self._uy = 0
        # Update Speed
        self._ux += self._ax
        self._uy += self._ay
        return self._x, self._y

    def updateAccelaration(self, ax, ay):
        self._ax = ax
        self._ay = ay

    def updateSpeed(self, ux, uy):
        self._ux = ux
        self._uy = uy

    def getWH(self):
        return self._width,self._height

    def getColor(self):
        return self._color,self._bgcolor

    def getShape(self):
        return self._shape

    