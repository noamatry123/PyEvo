__author__ = 'user-pc'
import pygame
import graphics
import classes
import random
import math
class pyAlgorithm:
    _counter=0
    __lastTimeSinceKey={"Left":0,"Right":0}
    __kinput=[]
    myCell=None
    myEggs=[]
    cellEggs=[]
    cellList=[]
    foodList=[]
    def __init__(self): #temp
        self.myCell=classes.baseCell(0,0,100,100,360,0,100,classes.Location(100,100),3,10,600,15)
        self.cellList.append(classes.baseCell(0,0,100,100,360,1,1,classes.Location(200,200),3,10,1200,15))
        self.cellEggs.append(classes.Egg((100,100),None,None,6))
        for i in xrange(10):
            self.putFood()
    def putFood(self):
        self.foodList.append(classes.Food(classes.Location(random.randint(0,800),random.randint(0,600)),10,5))
    def checkEat(self,cell):
        for food in self.foodList:
            if math.sqrt(((cell.location.x-food.location.x)**2)+((cell.location.y-food.location.y)**2))<cell.rad+food.rad:
                cell.eat(food)
                self.foodList.remove(food)


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
            if event.key==pygame.K_a:
                returnList.append("a")
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
        return returnList


    def nextStep(self):
        self._counter+=1
        ##handle input
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
        ##handle food and life
        self.checkEat(self.myCell)
        self.myCell.consumeFood(self._counter)
        self.myCell.consumeLife(self._counter)
        self.myCell.consumeEggTime(self._counter)
        self.myCell.checkRIP()
        for cell in self.cellList:
            self.checkEat(cell)
            cell.consumeFood(self._counter)
            cell.consumeLife(self._counter)
            cell.checkRIP()
            if cell.dead:
                self.cellList.remove(cell)
        if "a" in inputlist:
            if self.myCell.timeToLayLeft==0:
                self.myEggs.append(self.myCell.layEgg())
        self.__kinput=[]