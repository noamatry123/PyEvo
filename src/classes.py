__author__ = 'user-pc'
import graphics
import math
import algorithm
import pyEvoMain
import consts
from random import randint
import pygame

import easygui

curID=10
class Location:
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getTupple(self):
        return (self.x,self.y)
class practicle:
    loc=None
    color=None
    radius=None
    def __init__(self,loc,color,radius):
        self.loc=Location(loc.x,loc.y)
        self.color=color
        self.radius=radius
class Food:
    location=Location(0,0)
    amount=0
    rad=0
    image=None
    def __init__(self,location,amount,rad):
        self.location=location
        self.amount=amount
        self.rad=rad
        self.image=pygame.image.load('src/IMG/food.png')
    def getAmount(self):
        return self.amount
class Egg:
    location=Location(0,0)
    timeToHatch=0
    father=None
    mother=None
    rad=0
    Player = False
    image = None
    def __init__(self,flocation,father,mother,rad,timeToHatch,Player=False):
        self.location=Location(flocation.x,flocation.y)
        self.father=baseCell(father)
        self.mother=baseCell(mother)
        self.rad=rad
        self.timeToHatch=timeToHatch
        self.Player=Player
        self.image=pygame.image.load('src/IMG/egg.png')

    def Hatch(self): ##returns new cell to add ##
        if self.Player: ##Player cell egg hatching
            newCell = baseCell(self.mixPlayerCells(self.father,self.mother))
            newCell.location=Location(self.location.x, self.location.y)
            newCell=self.mutateCell(newCell,True)
            advance=self.chooseCell(newCell)
            return advance,newCell
        else: #normal cell hatching
            newCell = baseCell(self.mixNormalCells(self.father,self.mother))
            newCell.location=Location(self.location.x, self.location.y)
            newCell=self.mutateCell(newCell)
            return newCell
    def chooseCell(self,newCell):
        newtext="new\n"
        oldtext="old\n"
        newatt,oldatt=newCell.getOldNewAtts(),self.father.getOldNewAtts()
        for i in range(0,len(newatt)):
            newtext+=newatt[i]+"\n"
        for i in range(0,len(oldatt)):
            oldtext+=oldatt[i]+"\n"
        choice=None
        while choice not in ["Old","New"]:
            choice=graphics.askBoard("manualAuto",newtext,"Old","New",oldtext)
        if choice=="Old":
            return False
        return True
    def mutateCell(self,cell,Player=False):
        text=""
        #             Lay,eggW,car,foodW,life,lifeW,speed,AI,vision,eggH,strength
        mutationscale=[5,10,1,10,10,10,1,1,50,1,5]
        mutchance=[40,50,25,50,50,50,40,30,50,50,50]
        mutgoodbad=[50,50,60,50,40,50,50,60,30,50,50]

        for i in xrange(0,len(cell.getOldNewAtts())-1):
            randchance=randint(0,100)
            if randchance<mutchance[i]: ##mutate attribute
                if randint(0,100)<mutgoodbad[i]: #bad or good mutation
                    mutationscale[i]*=-1

                if i==0: ##timeToLay+left
                    cell.timeToLay+=mutationscale[i]
                    if cell.timeToLay<=0:
                        cell.timeToLay=5
                    if mutationscale[i]<0:
                        text+=str(cell.ID)+" mutated Timetolay by "+str(mutationscale[i])+"\n"
                    else:
                        text+=str(cell.ID)+" mutated Timetolay by "+str(mutationscale[i])+"\n"
                elif i==1: ##eggWithdraw
                    cell.eggwithdraw+=mutationscale[i]
                    if cell.eggwithdraw<=0:
                        cell.eggwithdraw=10
                    if mutationscale[i]<0:
                        text+=str(cell.ID)+" mutated eggWithdraw by "+str(mutationscale[i])+"\n"
                    else:
                        text+=str(cell.ID)+" mutated eggWithdraw by "+str(mutationscale[i])+"\n"
                elif i==2: ##carnivore
                    if mutationscale[i]<0:
                        cell.carnivore=0
                        text+=str(cell.ID)+" mutated carnivore negative\n"
                    else:
                        cell.carnivore=1
                        text+=str(cell.ID)+" mutated carnivore positive\n"
                elif i==3: ##foodWithdraw
                    cell.foodWithdraw+=mutationscale[i]
                    if cell.foodWithdraw<=0:
                        cell.foodWithdraw=10
                    if mutationscale[i]<0:
                        text+=str(cell.ID)+" mutated foodWithdraw by "+str(mutationscale[i])+"\n"
                    else:
                        text+=str(cell.ID)+" mutated foodWithdraw by "+str(mutationscale[i])+"\n"
                elif i==4: ##lifetime
                    cell.lifeTime+=mutationscale[i]
                    if cell.lifeTime<=0:
                        cell.lifeTime=5
                    if mutationscale[i]<0:
                        text+=str(cell.ID)+" mutated lifeTime by "+str(mutationscale[i])+"\n"
                    else:
                        text+=str(cell.ID)+" mutated lifeTime by "+str(mutationscale[i])+"\n"
                elif i==5: ##lifetimeWithdraw
                    cell.lifewithdraw+=mutationscale[i]
                    if cell.lifewithdraw<=0:
                        cell.lifewithdraw=10
                    if mutationscale[i]<0:
                        text+=str(cell.ID)+" mutated lifetimeWithdraw by "+str(mutationscale[i])+"\n"
                    else:
                        text+=str(cell.ID)+" mutated lifetimeWithdraw by "+str(mutationscale[i])+"\n"
                elif i==6: ##speed
                    cell.speed += mutationscale[i]
                    if cell.speed==5:
                        cell.speed=4
                    if cell.speed== 0:
                        cell.speed = 1
                    if mutationscale[i]<0:
                        text+=str(cell.ID)+" mutated speed by "+str(mutationscale[i])+"\n"
                    else:
                        text+=str(cell.ID)+" mutated speed by "+str(mutationscale[i])+"\n"
                elif i==7: ##AI
                    cell.AI += mutationscale[i]
                    if cell.AI == 5:
                        cell.AI = 4
                    if cell.AI == -1:
                        cell.AI = 0
                    if mutationscale[i]<0:
                        text+=str(cell.ID)+" mutated AI by "+str(mutationscale[i])+"\n"
                    else:
                        text+=str(cell.ID)+" mutated AI by "+str(mutationscale[i])+"\n"
                elif i==8: ##vision
                    cell.vision+=mutationscale[i]%consts.bigger(consts.screenwidth,consts.screenheight)
                    if cell.vision<=0:
                        cell.vision=50
                    if mutationscale[i]<0:
                        text+=str(cell.ID)+" mutated vision by "+str(mutationscale[i])+"\n"
                    else:
                        text+=str(cell.ID)+" mutated vision by "+str(mutationscale[i])+"\n"
                elif i==9: ##eggHatchTime
                    cell.eggHatchTime+=mutationscale[i]
                    if cell.eggHatchTime<=0:
                        cell.eggHatchTime=1
                    if mutationscale[i]<0:
                        text+=str(cell.ID)+" mutated eggHatchTime by "+str(mutationscale[i])+"\n"
                    else:
                        text+=str(cell.ID)+" mutated eggHatchTime by "+str(mutationscale[i])+"\n"
                elif i==10: ##strength
                    cell.strength+=mutationscale[i]
                    if cell.strength<=0:
                        cell.strength=5
                    if mutationscale[i]<0:
                        text+=str(cell.ID)+" mutated strength by "+str(mutationscale[i])+"\n"
                    else:
                        text+=str(cell.ID)+" mutated strength by "+str(mutationscale[i])+"\n"
        if Player:
            choice=None
            while choice!="Okay":
                choice=graphics.askBoard("Prompt",text)
        else:
            print text
        return cell
    def mixPlayerCells(self,mother,father):
        choice=None
        while choice not in ["Manual","Auto"]:
            choice=graphics.askBoard("manual","Manual or Auto?","Manual","Auto")
        if choice=="Auto":
            return self.mixNormalCells(mother,father)
        else: ## manual mode
            attIgnoreList=[0,4,7,11,12,16,17,18,19]
            print "\n\n"
            print "mixing cells manual"
            newCell=baseCell(father)
            for i in xrange(0,len(father.getAtts())):
                if i in attIgnoreList:
                    continue
                ##print colored("(1)","blue"), colored(father.getAtts()[i].ljust(25),"magenta"),
                ##print colored("(2)","blue"), colored(mother.getAtts()[i],"magenta")
                ##choice=raw_input()
                if i!=6:
                    fathertext=father.getAtts()[i]
                    mothertext=mother.getAtts()[i]
                    choice=None
                    while choice not in [fathertext,mothertext]:
                        choice=graphics.askBoard("manual","choose attribute",fathertext,mothertext)

                if i==1: ##timeToLay+left
                    if choice==fathertext:
                        newCell.timeToLay=father.timeToLay
                    else:
                        newCell.timeToLay=mother.timeToLay
                if i==2: ##eggWithdraw
                    if choice==fathertext:
                        newCell.eggwithdraw=father.eggwithdraw
                    else:
                        newCell.eggwithdraw=mother.eggwithdraw
                if i==3: ##carnivore
                    if choice==fathertext:
                        newCell.carnivore=father.carnivore
                    else:
                        newCell.carnivore=mother.carnivore
                if i==5: ##foodWithdraw
                    if choice==fathertext:
                        newCell.foodWithdraw=father.foodWithdraw
                    else:
                        newCell.foodWithdraw=mother.foodWithdraw
                if i==6: ##ID
                    newCell.ID=algorithm.getNextID()
                if i==8: ##lifetime
                    if choice==fathertext:
                        newCell.lifeTime=father.lifeTime
                    else:
                        newCell.lifeTime=mother.lifeTime
                if i==9: ##lifetimeWithdraw
                    if choice==fathertext:
                        newCell.lifewithdraw=father.lifewithdraw
                    else:
                        newCell.lifewithdraw=mother.lifewithdraw
                if i==10: ##speed
                    if choice==fathertext:
                        newCell.speed=father.speed
                    else:
                        newCell.speed=mother.speed
                if i==13: ##ai
                    if choice==fathertext:
                        newCell.AI=father.AI
                    else:
                        newCell.AI=mother.AI
                if i==14: ##vision
                    if choice==fathertext:
                        newCell.vision=father.vision
                    else:
                        newCell.vision=mother.vision
                if i==15: ##eggHatchTime
                    if choice==fathertext:
                        newCell.eggHatchTime=father.eggHatchTime
                    else:
                        newCell.eggHatchTime=mother.eggHatchTime
                if i==20: ##strength
                    if choice==fathertext:
                        newCell.strength=father.strength
                    else:
                        newCell.strength=mother.strength
        return newCell
    def mixNormalCells(self,mother,father):
        attIgnoreList=[0,4,7,11,12,16,17,18,19]
        print "\n\n"
        print "mixing normal cells"
        newCell=baseCell(father)
        for i in xrange(0,len(father.getAtts())):
            if i in attIgnoreList:
                continue

            fathertext=0

            choice=randint(0,1)

            if i==0: ##angle
                if choice==fathertext:
                    newCell.angle=father.angle
                else:
                    newCell.angle=mother.angle
            elif i==1: ##timeToLay+left
                if choice==fathertext:
                    newCell.timeToLay=father.timeToLay
                else:
                    newCell.timeToLay=mother.timeToLay
            elif i==2: ##eggWithdraw
                if choice==fathertext:
                    newCell.eggwithdraw=father.eggwithdraw
                else:
                    newCell.eggwithdraw=mother.eggwithdraw
            elif i==3: ##carnivore
                if choice==fathertext:
                    newCell.carnivore=father.carnivore
                else:
                    newCell.carnivore=mother.carnivore
            elif i==4: ##food
                newCell.food=50
            elif i==5: ##foodWithdraw
                if choice==fathertext:
                    newCell.foodWithdraw=father.foodWithdraw
                else:
                    newCell.foodWithdraw=mother.foodWithdraw
            elif i==6: ##ID
                newCell.ID=algorithm.getNextID()
            elif i==7: ##lastmother
                if choice==fathertext:
                    newCell.lastmother=father.lastmother
                else:
                    newCell.lastmother=mother.lastmother
            elif i==8: ##lifetime
                if choice==fathertext:
                    newCell.lifeTime=father.lifeTime
                else:
                    newCell.lifeTime=mother.lifeTime
            elif i==9: ##lifetimeWithdraw
                if choice==fathertext:
                    newCell.lifewithdraw=father.lifewithdraw
                else:
                    newCell.lifewithdraw=mother.lifewithdraw
            elif i==10: ##speed
                if choice==fathertext:
                    newCell.speed=father.speed
                else:
                    newCell.speed=mother.speed
            elif i==11: ##location
                if choice==fathertext:
                    newCell.location=father.location
                else:
                    newCell.location=mother.location
            elif i==12: ##rad
                if choice==fathertext:
                    newCell.rad=father.rad
                else:
                    newCell.rad=mother.rad
            elif i==13: ##ai
                if choice==fathertext:
                    newCell.AI=father.AI
                else:
                    newCell.AI=mother.AI
            elif i==14: ##vision
                if choice==fathertext:
                    newCell.vision=father.vision
                else:
                    newCell.vision=mother.vision
            elif i==15: ##eggHatchTime
                if choice==fathertext:
                    newCell.eggHatchTime=father.eggHatchTime
                else:
                    newCell.eggHatchTime=mother.eggHatchTime
            elif i==20: ##strength
                if choice==fathertext:
                    newCell.strength=father.strength
                else:
                    newCell.strength=mother.strength
        return newCell
    def consumeHatch(self,counter):
        if not self.timeToHatch==0: #egg is hatching
            if counter%consts.framerate==0:
                self.timeToHatch-=1
class spaceLimited:
    radius=0
    hurt=0
    active=False
    loc=None
    def __init__(self,radius,hurt):
        self.radius=radius
        self.hurt=hurt
        self.active=False
        consts.p2active=False
        self.loc=Location(consts.screenwidth/2,consts.screenheight/2)
    def activate(self):
        self.active=True
        consts.p2active=True
    def grow(self):
        if self.active==True:
            if self.radius>150:
                self.radius-=0.05
        consts.p2radius=self.radius
class AbCell:
    target=None
    lastCollision=None
    angle=0
    lifewithdraw=0
    carnivore=0##to do
    eggwithdraw=0
    food=0
    foodLeft=0
    foodWithdraw=0
    rad=0
    AI=0
    vision=0
    mode='m'
    ID=0
    lifeTime=0
    lifeTimeLeft=0
    location=Location(0,0)
    speed=0
    timeToLayLeft=0
    timeToLay=0
    timeToMove=0
    lastMother=None
    lastMotherHelper=None
    dead=False
    eggHatchTime=0
    strength=0
    timeToHurt=consts.framerate
    base90=None
    base45=None
    image=None
    bugMode=None
    def checkEat(self,foodList):
            for food in foodList:
                if math.sqrt(((self.location.x-food.location.x)**2)+((self.location.y-food.location.y)**2))<self.rad+food.rad:
                    self.eat(food)
                    foodList.remove(food)
    def changeAngle(self, dir):
        if not dir==0:
            self.angle=(self.angle+dir)%8 ##0 is up, clockwise (2 is right)
        if self.angle==0:
            self.image=pygame.transform.rotate(self.base90,180)
        elif self.angle==2:
            self.image=pygame.transform.rotate(self.base90,90)
        elif self.angle==4:
            self.image=pygame.transform.rotate(self.base90,0)
        elif self.angle==6:
            self.image=pygame.transform.rotate(self.base90,270)
        elif self.angle==1:
            self.image=pygame.transform.rotate(self.base45,270)
        elif self.angle==3:
            self.image=pygame.transform.rotate(self.base45,180)
        elif self.angle==5:
            self.image=pygame.transform.rotate(self.base45,90)
        elif self.angle==7:
            self.image=pygame.transform.rotate(self.base45,0)
    def eat(self, food):
        self.foodLeft+=food.getAmount()
        print self.ID, "ate food"
    def checkTarget(self):
        if self.target!=None:
            if math.sqrt(((self.location.x - self.target.location.x) ** 2) + (
                (self.location.y - self.target.location.y) ** 2)) < self.rad + self.target.rad:
                self.target=None
    def getAtts(self):
        list=[]
        list.append("angle: " +str(self.angle))
        list.append("timeToLay(Left): "+str(self.timeToLay) + "(" + str(self.timeToLayLeft)+")")
        list.append("eggWithDraw: "+str(self.eggwithdraw))
        list.append("carnivore: "+str(self.carnivore))
        list.append("food: "+str(self.food))
        list.append("foodWithdraw: "+str(self.foodWithdraw))
        list.append("ID: "+str(self.ID))
        if self.lastMother==None:
            list.append("lastmother: None")
        else:
            list.append("lastmother: "+str(self.lastMother.ID))
        list.append("lifeTime: "+str(self.lifeTime))
        list.append("lifeWithdraw: "+str(self.lifewithdraw))
        list.append("speed: "+str(self.speed))
        list.append("location: "+str(self.location.getTupple()))
        list.append("rad: "+str(self.rad))
        list.append("AI: "+str(self.AI))
        list.append("vision: "+str(self.vision))
        list.append("eggHatchTime: "+str(self.eggHatchTime))
        list.append(" ")
        list.append("foodLeft: "+str(self.foodLeft))
        list.append("lifeTimeLeft: "+str(self.lifeTimeLeft))
        list.append("mode : "+str(self.mode))
        list.append("strength: "+str(self.strength))
        return list
    def getUsefullAtts(self):
        list=[]
        list.append("foodLeft: "+str(self.foodLeft))
        list.append("lifeTimeLeft: "+str(self.lifeTimeLeft))
        list.append("timeToLay(Left): "+str(self.timeToLay) + "(" + str(self.timeToLayLeft)+")")
        list.append("carnivore: "+str(self.carnivore))
        list.append("ID: "+str(self.ID))
        if self.lastMother==None:
            list.append("lastmother: None")
        else:
            list.append("lastmother: "+str(self.lastMother.ID))
        list.append("speed: "+str(self.speed))
        list.append("eggHatchTime: "+str(self.eggHatchTime))
        list.append("mode : "+str(self.mode))
        list.append("strength: "+str(self.strength))
        return list
    def getOldNewAtts(self):
        list=[]
        list.append("timeToLay: "+str(self.timeToLay))
        list.append("eggWithDraw: "+str(self.eggwithdraw))
        list.append("carnivore: "+str(self.carnivore))
        list.append("foodWithdraw: "+str(self.foodWithdraw))
        list.append("lifeTime: "+str(self.lifeTime))
        list.append("lifeWithdraw: "+str(self.lifewithdraw))
        list.append("speed: "+str(self.speed))
        list.append("AI: "+str(self.AI))
        list.append("vision: "+str(self.vision))
        list.append("eggHatchTime: "+str(self.eggHatchTime))
        list.append("strength: "+str(self.strength))
        return list
    def layEgg(self,Player=False):
        egg=Egg(self.location,baseCell(self),baseCell(self.lastMother),6,self.eggHatchTime,Player)
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
        a=3
        b=4
        if self.speed==1:
            a=3
            b=4
        elif self.speed==2:
            a=4
            b=5
        elif self.speed==3:
            a=5
            b=6
        elif self.speed==4:
            a=6
            b=7
        if self.angle==0:#up
            self.location.y=(self.location.y-b)%consts.screenheight
        if self.angle==1:#up right
            self.location.y=(self.location.y-a)%consts.screenheight
            self.location.x=(self.location.x+a)%consts.screenwidth
        if self.angle==2:#right
            self.location.x=(self.location.x+b)%consts.screenwidth
        if self.angle==3:#down right
            self.location.y=(self.location.y+a)%consts.screenheight
            self.location.x=(self.location.x+a)%consts.screenwidth
        if self.angle==4:#down
            self.location.y=(self.location.y+b)%consts.screenheight
        if self.angle==5:#down left
            self.location.y=(self.location.y+a)%consts.screenheight
            self.location.x=(self.location.x-a)%consts.screenwidth
        if self.angle==6:#left
            self.location.x=(self.location.x-b)%consts.screenwidth
        if self.angle==7:#left up
            self.location.y=(self.location.y-a)%consts.screenheight
            self.location.x=(self.location.x-a)%consts.screenwidth
        """
        if self.timeToMove<=0:
            if self.angle==0:#up
                self.location.y=(self.location.y-4)%consts.screenheight
            elif self.angle==1:#up right
                self.location.y=(self.location.y-3)%consts.screenheight
                self.location.x=(self.location.x+3)%consts.screenwidth
            elif self.angle==2:#right
                self.location.x=(self.location.x+4)%consts.screenwidth
            elif self.angle==3:#down right
                self.location.y=(self.location.y+3)%consts.screenheight
                self.location.x=(self.location.x+3)%consts.screenwidth
            elif self.angle==4:#down
                self.location.y=(self.location.y+4)%consts.screenheight
            elif self.angle==5:#down left
                self.location.y=(self.location.y+3)%consts.screenheight
                self.location.x=(self.location.x-3)%consts.screenwidth
            elif self.angle==6:#left
                self.location.x=(self.location.x-4)%consts.screenwidth
            elif self.angle==7:#left up
                self.location.y=(self.location.y-3)%consts.screenheight
                self.location.x=(self.location.x-3)%consts.screenwidth
            self.timeToMove+=consts.framerate
        else:
            self.timeToMove-=self.speed
            """
    def consumeFood(self,tick):
        if tick%self.foodWithdraw==0:
            self.foodLeft-=1
    def consumeEggTime(self,tick):
        if tick%self.eggwithdraw==0 and self.timeToLayLeft>0:
            self.timeToLayLeft-=1
    def consumeLife(self,tick):
        if tick%self.lifewithdraw==0:
            self.lifeTimeLeft-=1
    def checkRIP(self):
        if self.lifeTimeLeft<=0:
            self.dead=True
            print str(self.ID), "Has died from old age."
        if self.foodLeft<=0:
            self.dead=True
            print str(self.ID), "Has died from hunger."

class baseCell(AbCell):
    def __init__(self,cell=None,angle=None,carnivore=None,eggwithdraw=None,foodLeft=None,foodWithdraw=None,ID=None,lifeTime=None,location=None,speed=None,rad=None,lifewithdraw=None,timeToLay=None,AI=None,vision=None,eggHatchTime=None,strength=0):
        if cell==None:
            self.lastCollision=None
            self.angle=angle
            self.AI=AI
            self.vision=vision
            self.lifewithdraw=lifewithdraw
            self.carnivore=carnivore
            self.timeToLay=timeToLay
            self.timeToLayLeft=timeToLay
            self.eggwithdraw=eggwithdraw
            self.food=foodLeft
            self.foodLeft=foodLeft
            self.foodWithdraw=foodWithdraw
            self.ID=ID
            self.rad=rad
            self.lifeTime=lifeTime
            self.lifeTimeLeft=lifeTime
            self.location=Location(location.x,location.y)
            self.speed=speed
            self.eggHatchTime=eggHatchTime
            self.mode='m'
            self.lastMother=None
            self.strength=strength
            self.base90, self.base45 = pygame.image.load('src/IMG/e_HeadD.png'),pygame.image.load('src/IMG/e_HeadUL.png')
            self.image=self.base90
        else:
            self.lastCollision=None
            self.angle=cell.angle
            self.AI=cell.AI
            self.vision=cell.vision
            self.lifewithdraw=cell.lifewithdraw
            self.carnivore=cell.carnivore
            self.timeToLay=cell.timeToLay
            self.timeToLayLeft=cell.timeToLay
            self.eggwithdraw=cell.eggwithdraw
            self.food=cell.food
            self.foodLeft=cell.food
            self.foodWithdraw=cell.foodWithdraw
            self.ID=cell.ID
            self.rad=cell.rad
            self.lifeTime=cell.lifeTime
            self.lifeTimeLeft=cell.lifeTime
            self.location=Location(cell.location.x,cell.location.y)
            self.speed=cell.speed
            self.eggHatchTime=cell.eggHatchTime
            self.mode='m'
            self.lastMother=None
            self.strength=cell.strength
            self.base90, self.base45 = pygame.image.load('src/IMG/e_HeadD.png'),pygame.image.load('src/IMG/e_HeadUL.png')
            self.image=self.base90