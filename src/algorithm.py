__author__ = 'user-pc'
import pygame
import classes
class pyAlgorithm:
    myCell=None
    __cellList=[]
    __foodList=[]
    __eggList=[]
    def __init__(self):
        self.myCell=classes.baseCell(0,0,100,100,1,1,1000,classes.Location(100,100),10)
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
        kinput=self.getInput()
        if "Left" in kinput:
            self.__myCell.changeAngle(-1)
        if "Right" in kinput:
            self.__myCell.changeAngle(1)
        if "Up" in kinput:
            self.__myCell.move()
