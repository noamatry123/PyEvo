__author__ = 'user-pc'
import graphics
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
    __timeToHatch=0
    __father=None
    __mother=None
    rad=0
    def __init__(self,location,father,mother,rad):
        self.location=Location(location[0],location[1])
        self.__father=father
        self._mother=mother
        self.rad=rad
    def Hatch(self):
        raise NotImplementedError
class AbCell:
    _angle=0
    _lifewithdraw=0
    _carnivore=0
    _eggwithdraw=0
    _food=0
    _foodWithdraw=0
    rad=0
    _ID=0
    _lifeTime=0
    location=Location(0,0)
    _speed=0
    timeToLayLeft=0
    _timeToLay=0
    _timeToMove=0
    _lastMother=None
    dead=False
    def changeAngle(self, dir):
        self._angle=(self._angle+dir)%8 ##0 is up, clockwise (2 is right)
    def eat(self, food):
        self._food+=food.getAmount()
        print "ate food"
    def getAtts(self):
        list=[]
        list.append("angle: " +str(self._angle))
        list.append("timeToLay(Left): "+str(self._timeToLay) + "(" + str(self.timeToLayLeft)+")")
        list.append("eggWithDraw: "+str(self._eggwithdraw))
        list.append("carnivore: "+str(self._carnivore))
        list.append("food: "+str(self._food))
        list.append("foodWithdraw: "+str(self._foodWithdraw))
        list.append("ID: "+str(self._ID))
        list.append("lastmother: "+str(self._lastMother))
        list.append("lifeTime: "+str(self._lifeTime))
        list.append("lifeWithdraw: "+str(self._lifewithdraw))
        list.append("speed: "+str(self._speed))
        list.append("location: "+str(self.location.getTupple()))
        list.append("rad: "+str(self.rad))
        return list
    def layEgg(self):
        if self._lastMother==None:
            egg=Egg(self.location.getTupple(),self,self._lastMother,6)
            self._lastMother=None
            self.timeToLayLeft=self._timeToLay
            print "layed egg"
            return egg
    def location_compensated(self): #for heading indicator
        compensated_x=self.location.x
        compensated_y=self.location.y
        if self._angle==0:#up
            compensated_y-=7
        elif self._angle==1:#up right
            compensated_y-=7
            compensated_x+=7
        elif self._angle==2:#right
            compensated_x+=7
        elif self._angle==3:#down right
            compensated_y+=7
            compensated_x+=7
        elif self._angle==4:#down
            compensated_y+=7
        elif self._angle==5:#down left
            compensated_y+=7
            compensated_x-=7
        elif self._angle==6:#left
            compensated_x-=7
        elif self._angle==7:#left up
            compensated_y-=7
            compensated_x-=7

        return compensated_x,compensated_y
    def move(self):
        if self._timeToMove==0:
            if self._angle==0:#up
                self.location.y=(self.location.y-4)%graphics.screenheight
            elif self._angle==1:#up right
                self.location.y=(self.location.y-3)%graphics.screenheight
                self.location.x=(self.location.x+3)%graphics.screenwidth
            elif self._angle==2:#right
                self.location.x=(self.location.x+4)%graphics.screenwidth
            elif self._angle==3:#down right
                self.location.y=(self.location.y+3)%graphics.screenheight
                self.location.x=(self.location.x+3)%graphics.screenwidth
            elif self._angle==4:#down
                self.location.y=(self.location.y+4)%graphics.screenheight
            elif self._angle==5:#down left
                self.location.y=(self.location.y+3)%graphics.screenheight
                self.location.x=(self.location.x-3)%graphics.screenwidth
            elif self._angle==6:#left
                self.location.x=(self.location.x-4)%graphics.screenwidth
            elif self._angle==7:#left up
                self.location.y=(self.location.y-3)%graphics.screenheight
                self.location.x=(self.location.x-3)%graphics.screenwidth
            self._timeToMove=self._speed
        else:
            self._timeToMove-=1
    def consumeFood(self,tick):
        if tick%self._foodWithdraw==0:
            self._food-=1
    def consumeEggTime(self,tick):
        if tick%self._eggwithdraw==0 and self.timeToLayLeft>0:
            self.timeToLayLeft-=1
    def consumeLife(self,tick):
        if tick%self._lifewithdraw==0:
            self._lifeTime-=1
    def checkRIP(self):
        if self._lifeTime<=0 or self._food<=0:
            self.dead=True

class baseCell(AbCell):
    def __init__(self,angle,carnivore,eggwithdraw,food,foodWithdraw,ID,lifeTime,location,speed,rad,lifewithdraw,timeToLay):
        self._angle=angle
        self._lifewithdraw=lifewithdraw
        self._carnivore=carnivore
        self._timeToLay=timeToLay
        self.timeToLayLeft=timeToLay
        self._eggwithdraw=eggwithdraw
        self._food=food
        self._foodWithdraw=foodWithdraw
        self._ID=ID
        self.rad=rad
        self._lifeTime=lifeTime
        self.location=location
        self._speed=speed
