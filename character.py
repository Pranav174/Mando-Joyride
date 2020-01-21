from stuff import stuff
from colorama import Fore

class character(stuff):
    def __init__(self):
        super().__init__()

    def takeInput(self, input):
        pass


class Mando(character):
    def __init__(self):
        super().__init__()
        self._shape = [
   "         .---.               ",
   "       .'_____`.             ",
   "       |~xxxxx~|             ",  
   "       |_  #  _|             ",
   "  .------`-#-'-----.         ",
   " (___|\_________/|_.`        ",
   "(  --< |\/    _\//|_ |       ", 
   "`.    ~----.-~=====,:========",
   " ~-._____/___:__(``/|        ",
   "    \__/======| /|           ",
   "    |_\|\    /|/_|           ",
   "    |_   \__/   _|           ",
   "    |  `'|  |`'  |           ",
   "    |    |  |    |           "]
        self._height = len(self._shape)
        self._width = len(self._shape[0])
        self._maxy = 53 - self._height -1
        self._maxx = 180 - self._width
        self._color = Fore.CYAN
        self._shieldActive = False
        self._shieldRemaining = 0
        self._reshield = 0

    def takeInput(self, input):
        if input=='w' and self._y!=self._miny:
            self._ay = -0.5
        elif self._y != self._maxx:
            self._ay = 0.1
        else:
            self.ay = 0
        if input=='a' and self._x != self._minx:
            self._ux = -5
        elif input=='d' and self._x != self._maxx:
            self._ux = 5
        else:
            self._ux = 0
        if self._reshield>0:
            self._reshield-=1
        if self._shieldActive:
            self._shieldRemaining-=1
            if self._shieldRemaining == 0:
                self._shieldActive = False
                self._color = Fore.CYAN

        if input==" " and not self._shieldActive and self._reshield==0:
            self._shieldActive=True
            self._shieldRemaining = 20*(10)
            self._color = Fore.GREEN
            self._reshield = 20*(40)
        
    def activateShield(self, time):
        if not self._shieldActive:
            self._shieldActive=True
            self._shieldRemaining = time
            self._color = Fore.MAGENTA

    def timeTillShield(self):
        return self._reshield
    
    def haveShield(self):
        return self._shieldActive

    def getXYspeed(self):
        return self._ux, self._uy

    def getXY(self):
        return self._x , self._y

    def getCenter(self):
        return self._x + self._width/2, self._y + self._height/2

    def getGunPoint(self):
        return self._x + self._width, self._y + 7

    def updatePosition(self,x,y):
        self._x += x
        self._y += y


class Dragon(character):
    def __init__(self, y,uy):
        super().__init__()
        self._shape = [
   "                          ",
   "                          ",
   "              _           ",
   "    o)/)_    /  \_        ",       
   "o^^^  _  \  /     \       ",       
   "'v!!!' !  \/   !   \      ",       
   "    ____/ ) '_ /  !  !    ",        
   "(/^===/   /!_ / . !       ",     
   "        !__ \  !_/ /      ",
   "        /    \   !/       ",
   "        ( /_   \_      _/)",       
   "    __)\ ^-__ ^^--^^ /    ",    
   "    'v--^'    ^^----^^    ",
   "                          ",]
        self._height = len(self._shape)
        self._width = len(self._shape[0])
        self._maxy = 53 - 14 -1
        self._x = 180
        self._y = y
        self._uy = uy
        self._color = Fore.RED
        self._lives = 10

    def takeInput(self, input):
        if input=='w' and self._y!=self._miny:
            self._ay = -0.5
        elif self._y != self._maxx:
            self._ay = 0.1
        else:
            self.ay = 0

    def getLives(self):
        return self._lives

    def reduceLives(self, count):
        self._lives -= count

    def getMouth(self):
        return self._x, self._y+4