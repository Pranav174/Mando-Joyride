from colorama import Back, Fore, Style
from stuff import stuff
from character import Mando,Dragon
from bullets import blasters, iceBalls
from obstacles import coins,bars,magnet,speedBoost, clouds
from datetime import datetime

def pos(x, y):
	return '\x1b[%d;%dH' % (y, x)

class session:
    def __init__(self):
        self.__score = 0
        self.__lives = 5
        self.__time = 100
        self.__initialTime = 100
        self.__framex = 204
        self.__framey = 53
        self.__frame = [[' ']*self.__framex]*self.__framey
        self.__objectList = []
        self.__mandoIndex = 0
        self.__frameCount = 0
        self.__availableMagnet = None
        self.__speedBoostActive = False
        self.__speedBoostTime = 50
        self.__dragonAppearance = self.__time - 75
        self.__obstaclesAllowed = self.__dragonAppearance+3
        self.__dragonActivated = False
        self.__dragon = None

    def addobject(self, obj):
        self.__objectList.append(obj)

    def getInitialFrame(self):
        self.__frame = [[' ' for i in range(self.__framex)] for j in range(self.__framey)]
        self.__frame[3] = self.replaceString(self.__frame[3], "WELCOME TO MANDO JOYRIDE") 
        self.__frame[5] = self.replaceString(self.__frame[5], "BY - PRANAV GOYAL") 
        self.__frame[9] = self.replaceString(self.__frame[9], "Controls:") 
        self.__frame[11] = self.replaceString(self.__frame[11], "Hold 'W' to use the Jetpack") 
        self.__frame[12] = self.replaceString(self.__frame[12], "Use 'A' and 'D' to move left and right") 
        self.__frame[13] = self.replaceString(self.__frame[13], "Press 'E' to shoot bullets (Unlimited Supply!!)") 
        self.__frame[14] = self.replaceString(self.__frame[14], "Press SpaceBar to activate Shield") 
        self.__frame[-8] = self.replaceString(self.__frame[-8], "[Press ENTER to start]") 
        self.__initialTime = datetime.now()
        self.__printFrame()
        

    def renderNextFrame(self):
        self.__frameCount+=1
        self.__time = 100 - (datetime.now() - self.__initialTime).total_seconds()
        self.__score += 0.1
        self.__makeEmptyGameFrame()
        self.__introduceObstacles()
        self.__magneticEffect()
        self.__checkSpeedBoost()
        self.__printObjects()
        self.__printFrame()

    def __introduceObstacles(self):
        if self.__time > self.__obstaclesAllowed:
            if self.__frameCount % 200 == 0:
                self.__objectList.append(magnet())
                self.__availableMagnet = self.__objectList[-1]
            elif self.__frameCount % 20 == 0:
                self.__objectList.append(bars())
            elif self.__frameCount % 130 == 0:
                self.__objectList.append(speedBoost())
            elif self.__frameCount % 10 == 0:
                self.__objectList.append(coins())
        elif self.__time < self.__dragonAppearance and not self.__dragonActivated:
            self.__dragonActivated = True
            x,y = self.__objectList[0].getXY()
            ux,uy = self.__objectList[0].getXYspeed()
            self.__objectList.append(Dragon(y,uy))
            self.__dragon = self.__objectList[-1]
        elif self.__dragonActivated and self.__frameCount % 10 ==0:
            x,y = self.__dragon.getMouth()
            self.__objectList.append(iceBalls(x,y))
        if self.__frameCount % 8 == 0:
            self.__objectList.append(clouds())

    
    def __makeEmptyGameFrame(self):
        self.__frame = [[' ' for i in range(self.__framex)] for j in range(self.__framey)]
        # self.__frame[0] = ['-']*self.__framex
        self.__frame[2] = self.replaceString(self.__frame[2], "SCORE : "+str(int(self.__score)), 30) 
        self.__frame[2] = self.replaceString(self.__frame[2], "LIVES : "+"|"*self.__lives) 
        self.__frame[2] = self.replaceString(self.__frame[2], "TIME : "+"{:.2f}".format(self.__time), 160) 
        if self.__speedBoostActive:
            self.__frame[3] = self.replaceString(self.__frame[3], "SPEED BOOST!!!",95) 
        if self.__dragonActivated:
            self.__frame[3] = self.replaceString(self.__frame[3], "Dragon Lives: "+"♡"*self.__dragon.getLives()) 
        if self.__objectList[0].timeTillShield()>0 and not self.__objectList[0].haveShield():
            self.__frame[3] = self.replaceString(self.__frame[3], "Shield will be back in: "+"{:.2f}".format(self.__objectList[0].timeTillShield()/20),5) 
        elif self.__objectList[0].haveShield():
            self.__frame[3] = self.replaceString(self.__frame[3], "Shield Active",5) 
        self.__frame[4] = ['-']*self.__framex
        self.__frame[-1] = ['-']*self.__framex

    def __printObjects(self):
        occupied = [[None for i in range(self.__framex)] for j in range(self.__framey)]
        for obj in self.__objectList:
            objx,objy = obj.getPOS(self.__speedBoostActive)
            objx = int(objx)
            objy = int(objy)
            width, height = obj.getWH()
            shape = obj.getShape()
            color, bgcolor = obj.getColor()
            visible = False
            for x in range(width):
                for y in range(height):
                    if 0<= (objy+y) < self.__framey and 0 <= (objx+x) < self.__framex and shape[y][x] != " ":
                        if occupied[objy+y][objx+x]!=None:
                            self.__handleCollision(occupied[objy+y][objx+x], obj)
                        self.__frame[objy+y][objx+x] = (shape[y][x],color,bgcolor)
                        visible = True
                        occupied[objy+y][objx+x] = obj
            if not visible:
                self.removeObject(obj)

    def __magneticEffect(self):
        if isinstance(self.__availableMagnet, magnet) and self.__availableMagnet in self.__objectList:
            magx,magy = self.__availableMagnet.getCenter()
            mandox, mandoy = self.__objectList[0].getCenter()
            x = -1
            if mandox < magx:
                x = 1
            elif mandox == magx:
                x = 0
            y = -0.2
            if mandoy < magy:
                y = 0.2
            elif mandoy == magy:
                y = 0
            self.__objectList[0].updatePosition(x,y)
            
    def __checkSpeedBoost(self):
        if self.__speedBoostActive:
            self.__speedBoostTime-=1
            if self.__speedBoostTime==0:
                self.__speedBoostActive = False

    def setInput(self, input):
        if input=='e':
            x,y = self.__objectList[0].getGunPoint()
            self.__objectList.append(blasters(x,y))
        self.__objectList[self.__mandoIndex].takeInput(input)
        if self.__dragonActivated:
            self.__dragon.takeInput(input)
            

    def getFinalFram(self):
        self.__frame = [[' ']*self.__framex]*self.__framey
        reason = self.endGame()
        explanation = "You pressed 'q'"
        if reason == 1:
            explanation = "Congrates, You destroyed the dragon"
        elif reason == 2:
            explanation = "You ran out of Lives"
        elif reason == 3:
            explanation = "You ran out of Time"
        self.__frame[int(self.__framey/2)-2] = self.replaceString(self.__frame[int(self.__framey/2)-2], explanation) 
        self.__frame[int(self.__framey/2)-1] = self.replaceString(self.__frame[int(self.__framey/2)-1], "Score = "+ str(int(self.__score))) 
        self.__frame[int(self.__framey/2)] = self.replaceString(self.__frame[int(self.__framey/2)], "THANKS FOR PLAYING THE GAME") 
        self.__frame[int(self.__framey/2)+2] = self.replaceString(self.__frame[int(self.__framey/2)+2], "By - Pranav Goyal") 
        self.__printFrame()

    def __printFrame(self):
        print(pos(0,0),sep="", end='')
        for j in range(self.__framey):
            for i in range(self.__framex):
                pixel = self.__frame[j][i]
                try:
                    char,color,bgcolor = pixel
                except:
                    char = pixel
                    color = Fore.WHITE
                    bgcolor = Back.BLACK
                print(color,bgcolor,char, end="",sep="")
            print()

    def __handleCollision(self, obj1, obj2):
        if self.__isPairof(obj1,obj2,Mando,coins):
            if not obj2.isEaten():
                self.__score+=10
                obj2.eat()
                self.removeObject(obj2)
        if self.__isPairof(obj1,obj2,Mando,bars) or self.__isPairof(obj1,obj2,Mando,iceBalls):
            if not obj1.haveShield():
                self.__lives-=1
                obj1.activateShield(20)
        if self.__isPairof(obj1,obj2,blasters,bars):
            self.removeObject(obj1)
            self.removeObject(obj2)
        if self.__isPairof(obj1,obj2,Mando,speedBoost):
            self.removeObject(obj2)
            self.__speedBoostActive = True
            self.__speedBoostTime = 20 * 5
        if self.__isPairof(obj1,obj2,blasters,Dragon):
            try:
                if isinstance(obj1, blasters):
                    self.__objectList.remove(obj1)
                    obj2.reduceLives(1)
                else:
                    self.__objectList.remove(obj2)
                    obj1.reduceLives(1)
            except:
                pass
        if self.__isPairof(obj1, obj2, blasters, iceBalls):
            self.removeObject(obj1)
            self.removeObject(obj2)

    def __isPairof(self,obj1,obj2,class1,class2):
        return (isinstance(obj1,class1) and isinstance(obj2,class2)) or (isinstance(obj1,class2) and isinstance(obj2,class1))
    
    def removeObject(self,obj):
        try:
            self.__objectList.remove(obj)
        except:
            pass

    def replaceString(self, original, change, pos = -1):
        if pos == -1:
            pos = int((len(original) - len(change))/2)
        change = list(change)
        return original[0:pos] + change + original[pos+len(change):]

    def endGame(self):
        if self.__dragonActivated:
            if self.__dragon.getLives() <= 0:
                return 1
        if self.__lives <= 0:
            return 2
        if self.__time <= 0:
            return 3
        return 0