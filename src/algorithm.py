__author__ = 'user-pc'
import pygame
import classes
class pyAlgorithm:
    __myCell=None
    __cellList=[]
    __foodList=[]
    __eggList=[]
    def __init__(self):
        self.__myCell=classes.AbCell()
    def getInput(self):
        returnList=[]
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            returnList.append("Left")
        if key[pygame.K_RIGHT]:
            returnList.append("Right")
        if key[pygame.K_UP]:
            returnList.append("Up")
        if key[pygame.DOWN]:
            returnList.append("Down")
        return returnList
    def nextStep(self):
