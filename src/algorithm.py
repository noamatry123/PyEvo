__author__ = 'user-pc'
import pygame
import graphics
import classes
import consts
import random
import math
import AI

def getNextID():
    classes.curID+=1
    return classes.curID
class pyAlgorithm:
    _counter=0
    __lastTimeSinceKey={"Left":0,"Right":0}
    __kinput=[]
    myCell=None
    myEggs=[]
    cellEggs=[]
    cellList=[]
    foodList=[]
    screenwidth=0
    screenheight=0
    framerate=100
    def __init__(self,height,width): #temp
        ##(cell,angle,carnivore,eggwithdraw,food,foodWithdraw,ID,lifeTime,location,speed,rad,lifewithdraw,timeToLay,AI,vision,eggHatchTime,strength=0):
        self.screenheight=height
        self.screenwidth=width
        angle=0
        lifewithdraw=self.framerate
        carnivore=0
        eggwithdraw=self.framerate
        food=30
        foodWithdraw=self.framerate
        rad=10
        AI=0
        vision=50
        lifeTime=20
        speed=15
        timeToLay=1
        eggHatchTime=3
        strength=10
        self.myCell=classes.baseCell(None,angle,1,eggwithdraw,food,foodWithdraw,0,50,classes.Location(400,400),speed,rad,lifewithdraw,timeToLay,AI,vision,eggHatchTime,strength)
        self.cellList.append(classes.baseCell(None,angle,carnivore,eggwithdraw,food,foodWithdraw,1,lifeTime,classes.Location(random.randint(0,self.screenwidth),random.randint(0,self.screenheight)),speed,rad,lifewithdraw,timeToLay,AI,vision,eggHatchTime,strength))
        self.cellList.append(classes.baseCell(None,angle,carnivore,eggwithdraw,food,foodWithdraw,2,lifeTime,classes.Location(random.randint(0,self.screenwidth),random.randint(0,self.screenheight)),speed,rad,lifewithdraw,timeToLay,AI,vision,eggHatchTime,strength))
        self.cellList.append(classes.baseCell(None,angle,carnivore,eggwithdraw,food,foodWithdraw,3,lifeTime,classes.Location(random.randint(0,self.screenwidth),random.randint(0,self.screenheight)),speed,rad,lifewithdraw,timeToLay,AI,vision,eggHatchTime,strength))
        self.cellList.append(classes.baseCell(None,angle,carnivore,eggwithdraw,food,foodWithdraw,4,lifeTime,classes.Location(random.randint(0,self.screenwidth),random.randint(0,self.screenheight)),speed,rad,lifewithdraw,timeToLay,AI,vision,eggHatchTime,strength))
        self.cellList.append(classes.baseCell(None,angle,carnivore,eggwithdraw,food,foodWithdraw,5,lifeTime,classes.Location(random.randint(0,self.screenwidth),random.randint(0,self.screenheight)),speed,rad,lifewithdraw,timeToLay,AI,vision,eggHatchTime,strength))
        self.cellList.append(classes.baseCell(None,angle,carnivore,eggwithdraw,food,foodWithdraw,6,lifeTime,classes.Location(random.randint(0,self.screenwidth),random.randint(0,self.screenheight)),speed,rad,lifewithdraw,timeToLay,AI,vision,eggHatchTime,strength))
        self.cellList.append(classes.baseCell(None,angle,carnivore,eggwithdraw,food,foodWithdraw,7,lifeTime,classes.Location(random.randint(0,self.screenwidth),random.randint(0,self.screenheight)),speed,rad,lifewithdraw,timeToLay,AI,vision,eggHatchTime,strength))
        self.cellList.append(classes.baseCell(None,angle,carnivore,eggwithdraw,food,foodWithdraw,8,lifeTime,classes.Location(random.randint(0,self.screenwidth),random.randint(0,self.screenheight)),speed,rad,lifewithdraw,timeToLay,AI,vision,eggHatchTime,strength))
        self.cellList.append(classes.baseCell(None,angle,carnivore,eggwithdraw,food,foodWithdraw,9,lifeTime,classes.Location(random.randint(0,self.screenwidth),random.randint(0,self.screenheight)),speed,rad,lifewithdraw,timeToLay,AI,vision,eggHatchTime,strength))
        self.cellList.append(classes.baseCell(None,angle,carnivore,eggwithdraw,food,foodWithdraw,10,lifeTime,classes.Location(random.randint(0,self.screenwidth),random.randint(0,self.screenheight)),speed,rad,lifewithdraw,timeToLay,AI,vision,eggHatchTime,strength))
        self.cellEggs.append(self.cellList[0].layEgg())
        ##self.cellEggs[0].mixPlayerCells(self.myCell,self.myCell)
        ##self.cellEggs.append(classes.Egg((100,100),self.cellList[0],None,6,0))
        for i in xrange(10):
            self.putFood()

    def putFood(self):
        self.foodList.append(classes.Food(classes.Location(random.randint(0,self.screenwidth),random.randint(0,self.screenheight)),10,5))
    def growCellEggs(self):
        for egg in self.cellEggs:
            if egg.timeToHatch==0:
                newCell=egg.Hatch()
                self.cellList.append(newCell)
                self.cellEggs.remove(egg)
    def growPlayerEggs(self):
        for egg in self.myEggs:
            if egg.timeToHatch==0:
                advance,newCell=egg.Hatch()
                if advance:
                    self.cellList.append(self.myCell)
                    self.myEggs.remove(egg)
                    self.myCell=newCell
                else:
                    self.cellList.append(newCell)
                    self.myEggs.remove(egg)
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
            if event.key==pygame.K_c:
                returnList.append("c")
            if event.key==pygame.K_p:
                pygame.event.post(pygame.QUIT)
        key=pygame.key.get_pressed()
        #check for hold
        if key[pygame.K_LEFT]:
            if self.__lastTimeSinceKey["Left"]>consts.framerate/11:
                returnList.append("OLeft")
                self.__lastTimeSinceKey["Left"]=0
            else:
                self.__lastTimeSinceKey["Left"]+=1
        if key[pygame.K_RIGHT]:
            if self.__lastTimeSinceKey["Right"]>consts.framerate/11:
                returnList.append("ORight")
                self.__lastTimeSinceKey["Right"]=0
            else:
                self.__lastTimeSinceKey["Right"]+=1
        #check up and down
        if key[pygame.K_UP]:
            returnList.append("Up")
        return returnList


    def nextStep(self,text):
        if text!="Empty":
            consts.askingQuestion=False
            ##parse input


        self._counter+=1
        ##handle input
        inputlist=self.getInput()
        for item in inputlist:
            if (item=="Left" or item=="Right") and (("Left" in self.__kinput) or ("Right" in self.__kinput)):
                continue
            elif (item=="c" and ("c" in self.__kinput)):
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
        self.myCell.checkEat(self.foodList)
        self.myCell.consumeFood(self._counter)
        self.myCell.consumeLife(self._counter)
        self.myCell.consumeEggTime(self._counter)
        self.myCell.checkRIP()
        if self.myCell.timeToHurt!=0:
            self.myCell.timeToHurt-=1
        input=[]
        for cell in self.cellList:
            input=AI.nextStep(self.myCell,self.cellList,self.foodList,cell)
            for item in input:
                if item=="OLeft":
                    cell.changeAngle(-1)
                if item=="ORight":
                    cell.changeAngle(1)
                if "Up" in input:
                    cell.move()
                if "a" in input:
                    if cell.timeToLayLeft==0:
                        self.cellEggs.append(cell.layEgg())
            cell.checkEat(self.foodList)
            cell.consumeFood(self._counter)
            cell.consumeLife(self._counter)
            cell.consumeEggTime(self._counter)
            cell.checkRIP()
            if cell.timeToHurt!=0:
                cell.timeToHurt-=1
            if cell.dead:
                self.cellList.remove(cell)


        if "a" in inputlist:
            if self.myCell.timeToLayLeft==0:
                self.myEggs.append(self.myCell.layEgg(True))

        if "c" in inputlist: ##carnivore or mating
            if self.myCell.mode=='m':
                self.myCell.mode='c'
            else:
                self.myCell.mode='m'

        ##check egg hatching
        for egg in self.cellEggs:
            egg.consumeHatch(self._counter)
        for egg in self.myEggs:
            egg.consumeHatch(self._counter)
        self.growCellEggs()
        self.growPlayerEggs()

        ##check for carnivore eating and mating
        allCells=[]
        for cell in self.cellList:
            allCells.append(cell)
        allCells.append(self.myCell)
        for cell in allCells:
            for otherCell in allCells:
                collision=math.sqrt(((cell.location.x-otherCell.location.x)**2)+((cell.location.y-otherCell.location.y)**2))<cell.rad+otherCell.rad
                if (cell.ID!=otherCell.ID) and (collision): ##not the same cell
                    if cell.mode=='c': ##carnivore
                        if otherCell.timeToHurt<=0:
                            otherCell.timeToHurt=consts.framerate
                            otherCell.lifeTimeLeft-=cell.strength
                            if otherCell.lifeTimeLeft<=0: ##only eat if you killed him
                                cell.foodLeft+=otherCell.foodLeft
                                otherCell.lifeTimeLeft=0
                                otherCell.dead=True
                                print str(cell.ID), "Ate", str(otherCell.ID)
                            else: ##cant eat
                                print str(cell.ID), "hurt", str(otherCell.ID), "but did not kill him."
                    if cell.mode=='m': ##mate
                        if otherCell.mode=='m' and not (cell.lastMother.ID==otherCell.ID): ##mate too
                            cell.lastMother=classes.baseCell(otherCell)
                            otherCell.lastMother=classes.baseCell(cell)


        #grow more food
        if self._counter%consts.framerate%6.6==0:
            self.putFood()
        self.__kinput=[]