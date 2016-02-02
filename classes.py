__author__ = 'user-pc'
class Location:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    x=0
    y=0
class Food:

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
    def changeAngle(self, dir):
        self.__angle+=dir
    def eat(self, food):
