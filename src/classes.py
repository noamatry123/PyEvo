__author__ = 'user-pc'
import graphics
import math
import algorithm

curID=0
class Location:
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getTupple(self):
        return (self.x,self.y)
class Food:
    location=Location(0,0)
    amount=0
    rad=0
    def __init__(self,location,amount,rad):
        self.location=location
        self.amount=amount
        self.rad=rad
    def getAmount(self):
        return self.amount
class Egg:

    location=Location(0,0)
    timeToHatch=0
    __father=None
    __mother=None
    rad=0
    def __init__(self,location,father,mother,rad,timeToHatch):
        self.location=Location(location[0],location[1])
        self.__father=baseCell(father)
        self._mother=mother
        self.rad=rad
        self.timeToHatch=timeToHatch
    def Hatch(self): ##returns new cell to add ##
        newCell = baseCell(self.__father)
        newCell.location=Egg.location
        return newCell
class AbCell:
    angle=0
    lifewithdraw=0
    carnivore=0##to do
    eggwithdraw=0
    food=0
    foodWithdraw=0
    rad=0
    AI=0
    vision=0
    ID=0
    lifeTime=0
    location=Location(0,0)
    speed=0
    timeToLayLeft=0
    timeToLay=0
    timeToMove=0
    lastMother=None
    dead=False
    eggHatchTime=10
    def checkEat(self,foodList):
            for food in foodList:
                if math.sqrt(((self.location.x-food.location.x)**2)+((self.location.y-food.location.y)**2))<self.rad+food.rad:
                    self.eat(food)
                    foodList.remove(food)
    def changeAngle(self, dir):
        self.angle=(self.angle+dir)%8 ##0 is up, clockwise (2 is right)
    def eat(self, food):
        self.food+=food.getAmount()
        print "ate food"
    def getAtts(self):
        list=[]
        list.append("angle: " +str(self.angle))
        list.append("timeToLay(Left): "+str(self.timeToLay) + "(" + str(self.timeToLayLeft)+")")
        list.append("eggWithDraw: "+str(self.eggwithdraw))
        list.append("carnivore: "+str(self.carnivore))
        list.append("food: "+str(self.food))
        list.append("foodWithdraw: "+str(self.foodWithdraw))
        list.append("ID: "+str(self.ID))
        list.append("lastmother: "+str(self.lastMother))
        list.append("lifeTime: "+str(self.lifeTime))
        list.append("lifeWithdraw: "+str(self.lifewithdraw))
        list.append("speed: "+str(self.speed))
        list.append("location: "+str(self.location.getTupple()))
        list.append("rad: "+str(self.rad))
        return list
    def layEgg(self):
        if self.lastMother==None:
            egg=Egg(self.location.getTupple(),baseCell(self),self.lastMother,6,0)
            self.lastMother=None
            self.timeToLayLeft=self.timeToLay
            print self.ID , "layed egg."
            return egg
    def location_compensated(self): #for heading indicator
        compensated_x=self.location.x
        compensated_y=self.location.y
        if self.angle==0:#up
            compensated_y-=7
        elif self.angle==1:#up right
            compensated_y-=7
            compensated_x+=7
        elif self.angle==2:#right
            compensated_x+=7
        elif self.angle==3:#down right
            compensated_y+=7
            compensated_x+=7
        elif self.angle==4:#down
            compensated_y+=7
        elif self.angle==5:#down left
            compensated_y+=7
            compensated_x-=7
        elif self.angle==6:#left
            compensated_x-=7
        elif self.angle==7:#left up
            compensated_y-=7
            compensated_x-=7

        return compensated_x,compensated_y
    def move(self):
        if self.timeToMove==0:
            if self.angle==0:#up
                self.location.y=(self.location.y-4)%graphics.screenheight
            elif self.angle==1:#up right
                self.location.y=(self.location.y-3)%graphics.screenheight
                self.location.x=(self.location.x+3)%graphics.screenwidth
            elif self.angle==2:#right
                self.location.x=(self.location.x+4)%graphics.screenwidth
            elif self.angle==3:#down right
                self.location.y=(self.location.y+3)%graphics.screenheight
                self.location.x=(self.location.x+3)%graphics.screenwidth
            elif self.angle==4:#down
                self.location.y=(self.location.y+4)%graphics.screenheight
            elif self.angle==5:#down left
                self.location.y=(self.location.y+3)%graphics.screenheight
                self.location.x=(self.location.x-3)%graphics.screenwidth
            elif self.angle==6:#left
                self.location.x=(self.location.x-4)%graphics.screenwidth
            elif self.angle==7:#left up
                self.location.y=(self.location.y-3)%graphics.screenheight
                self.location.x=(self.location.x-3)%graphics.screenwidth
            self.timeToMove=self.speed
        else:
            self.timeToMove-=1
    def consumeFood(self,tick):
        if tick%self.foodWithdraw==0:
            self.food-=1
    def consumeEggTime(self,tick):
        if tick%self.eggwithdraw==0 and self.timeToLayLeft>0:
            self.timeToLayLeft-=1
    def consumeLife(self,tick):
        if tick%self.lifewithdraw==0:
            self.lifeTime-=1
    def checkRIP(self):
        if self.lifeTime<=0:
            self.dead=True
            print str(self.ID), "Has died from old age."
        if self.food<=0:
            self.dead=True
            print str(self.ID), "Has died from hunger."

class baseCell(AbCell):
    def __init__(self,cell=None,angle=None,carnivore=None,eggwithdraw=None,food=None,foodWithdraw=None,ID=None,lifeTime=None,location=None,speed=None,rad=None,lifewithdraw=None,timeToLay=None,AI=None,vision=None):
        if cell==None:
            self.angle=angle
            self.AI=AI
            self.vision=vision
            self.lifewithdraw=lifewithdraw
            self.carnivore=carnivore
            self.timeToLay=timeToLay
            self.timeToLayLeft=timeToLay
            self.eggwithdraw=eggwithdraw
            self.food=food
            self.foodWithdraw=foodWithdraw
            self.ID=algorithm.getNextID()
            self.rad=rad
            self.lifeTime=lifeTime
            self.location=Location(location.x,location.y)
            self.speed=speed
        else:
            self.angle=cell.angle
            self.AI=cell.AI
            self.vision=cell.vision
            self.lifewithdraw=cell.lifewithdraw
            self.carnivore=cell.carnivore
            self.timeToLay=cell.timeToLay
            self.timeToLayLeft=cell.timeToLay
            self.eggwithdraw=cell.eggwithdraw
            self.food=cell.food
            self.foodWithdraw=cell.foodWithdraw
            self.ID=algorithm.getNextID()
            self.rad=cell.rad
            self.lifeTime=cell.lifeTime
            self.location=Location(cell.location.x,cell.location.y)
            self.speed=cell.speed