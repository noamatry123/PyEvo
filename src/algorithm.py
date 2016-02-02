__author__ = 'user-pc'
import pygame
import graphics
import classes
class pyAlgorithm:
    __runtime=0 #for input
    __kinput=[]
    myCell=None
    __cellList=[]
    __foodList=[]
    __eggList=[]
    def __init__(self): #temp
        self.myCell=classes.baseCell(0,0,100,100,1,5,1000,classes.Location(100,100),10)
    def getInput(self):
        returnList=[]
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            returnList.append("Left")
        if key[pygame.K_RIGHT]:
            returnList.append("Right")
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
        if self.__runtime>15:
            if "Left" in self.__kinput:
                self.myCell.changeAngle(-1)
            if "Right" in self.__kinput:
                self.myCell.changeAngle(1)
            self.__kinput=[]
            self.__runtime=0
        if "Up" in self.__kinput:
            self.myCell.move()
        self.__runtime+=1