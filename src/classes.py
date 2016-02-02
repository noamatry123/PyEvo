__author__ = 'user-pc'
class Location:
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getTupple(self):
        return (self.x,self.y)
class Food:
    __location=Location(0,0)
    __amount=0
    def __init__(self,location,amount):
        self.__location=location
        self.__amount=amount
    def getAmount(self):
        return self.__amount
class Egg:
    __location=Location(0,0)
    __timeToHatch=0
    __father=None
    __mother=None
    def __init__(self,location,father,mother):
        self.__location=location
        self.__father=father
        self._mother=mother
    def Hatch(self):
        raise NotImplementedError
class AbCell:
    _angle=0
    _carnivore=0
    _eggCycle=0
    _eggs=[]
    _food=0
    _foodWithdraw=0
    _ID=0
    _lifeTime=0
    location=Location(0,0)
    _speed=0
    _timeToLay=0
    _timeToMove=0
    _lastMother=None
    def changeAngle(self, dir):
        self._angle=(self._angle+dir)%8 ##0 is up, clockwise (2 is right)
    def eat(self, food):
        self.food+=food.getAmount()
    def layEgg(self):
        self._timeToLay=self._eggCycle
        if self._lastMother!=None:
            self._eggs.append(Egg(self.location,self,self._lastMother))
            self._lastMother=None
    def move(self):
        if self._timeToMove==0:
            if self._angle==0:#up
                self.location.y-=1
            elif self._angle==1:#up right
                self.location.y-=1
                self.location.x+=1
            elif self._angle==2:#right
                self.location.x+=1
            elif self._angle==3:#down right
                self.location.y+=1
                self.location.x+=1
            elif self._angle==4:#down
                self.location.y+=1
            elif self._angle==5:#down left
                self.location.y+=1
                self.location.x-=1
            elif self._angle==6:#left
                self.location.x-=1
            elif self._angle==7:#left up
                self.location.y-=1
                self.location.x-=1
        else:
            self._timeToMove-=1
class baseCell(AbCell):
    def __init__(self,angle,carnivore,eggCycle,food,foodWithdraw,ID,lifeTime,location,speed):
        self._angle=angle
        self._carnivore=carnivore
        self._eggCycle=eggCycle
        self._food=food
        self._foodWithdraw=foodWithdraw
        self._ID=ID
        self._lifeTime=lifeTime
        self._location=location
        self._speed=speed
