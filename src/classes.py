__author__ = 'user-pc'
class Location:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    x=0
    y=0
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
        self.__mother=mother
    def Hatch(self):
        raise NotImplementedError
class AbCell:
    __angle=0
    __carnivore=0
    __eggCycle=0
    __eggs=[]
    __food=0
    __foodWithdraw=0
    __ID=0
    __lifeTime=0
    __location=Location(0,0)
    __speed=0
    __timeToLay=0
    __timeToMove=0
    __lastMother=None
    def changeAngle(self, dir):
        self.__angle=(self.__angle+dir)%8 ##0 is up, clockwise (2 is right)
    def eat(self, food):
        self.food+=food.getAmount()
    def layEgg(self):
        self.__timeToLay=self.__eggCycle
        if self.__lastMother!=None:
            self.__eggs.append(Egg(self.__location,self,self.__lastMother))
            self.__lastMother=None
    def nextStep(self):
        if self.__timeToMove==0:
            if self.__angle==0:
                self.__location[1]-=1
            elif self.__angle==1:
                self.__location[1]-=1
                self.__location[0]+=1