__author__ = 'user-pc'
import pygame
import graphics
import classes
class pyAlgorithm:
    __kinput=[]
    myCell=None
    __cellList=[]
    __foodList=[]
    __eggList=[]
    def __init__(self): #temp
        self.myCell=classes.baseCell(0,0,100,100,1,5,1000,classes.Location(100,100),10)
    def getInput(self):
        returnList=[]
        for event in pygame.event.get(pygame.KEYDOWN):
            if event.key==pygame.K_LEFT:
                returnList.append("Left")
            if event.key==pygame.K_RIGHT:
                returnList.append("Right")
        key=pygame.key.get_pressed()
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
            if item=="Left":
                self.myCell.changeAngle(-1)
            if item=="Right":
                self.myCell.changeAngle(1)
        if "Up" in self.__kinput:
            self.myCell.move()
        self.__kinput=[]