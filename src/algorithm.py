__author__ = 'user-pc'
import pygame
import graphics
import classes
class pyAlgorithm:
    __lastTimeSinceKey={"Left":0,"Right":0}
    __kinput=[]
    myCell=None
    cellList=[]
    foodList=[]
    __eggList=[]
    def __init__(self): #temp
        self.myCell=classes.baseCell(0,0,100,100,1,5,1000,classes.Location(100,100),3)
        self.cellList.append(classes.baseCell(0,0,100,100,1,5,1000,classes.Location(200,200),3))

    def putFood(self):
        self.foodList.append(classes.Food(classes.Location(rand,rand)))
    def getInput(self):
        returnList=[]
        events = pygame.event.get(pygame.KEYDOWN)
        for event in events:
            if event.key==pygame.K_LEFT:
                returnList.append("Left")
                self.__lastTimeSinceKey["Left"]=0
            if event.key==pygame.K_RIGHT:
                returnList.append("Right")
                self.__lastTimeSinceKey["Right"]=0
        key=pygame.key.get_pressed()
        #check for hold
        if key[pygame.K_LEFT]:
            if self.__lastTimeSinceKey["Left"]>17:
                returnList.append("OLeft")
                self.__lastTimeSinceKey["Left"]=0
            else:
                self.__lastTimeSinceKey["Left"]+=1
        if key[pygame.K_RIGHT]:
            if self.__lastTimeSinceKey["Right"]>17:
                returnList.append("ORight")
                self.__lastTimeSinceKey["Right"]=0
            else:
                self.__lastTimeSinceKey["Right"]+=1
        #check up and down
        if key[pygame.K_UP]:
            returnList.append("Up")
        if key[pygame.K_DOWN]:
            returnList.append("Down")
        return returnList
    def nextStep(self):
        inputlist=self.getInput()
        for item in inputlist:
            if (item=="Left" or item=="Right") and (("Left" in self.__kinput) or ("Right" in self.__kinput)):
                continue
            else:
                self.__kinput.append(item)
        for item in self.__kinput:
            if item=="Left" or item=="OLeft":
                self.myCell.changeAngle(-1)
            if item=="Right" or item=="ORight":
                self.myCell.changeAngle(1)
        if "Up" in self.__kinput:
            self.myCell.move()
        self.__kinput=[]