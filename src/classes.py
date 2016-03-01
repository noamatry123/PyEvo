__author__ = 'user-pc'
import graphics
import math
import algorithm
import pyEvoMain
from random import randint


import easygui

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
    father=None
    mother=None
    rad=0
    Player = False
    def __init__(self,flocation,father,mother,rad,timeToHatch,Player=False):
        self.location=Location(flocation.x,flocation.y)
        self.father=baseCell(father)
        self.mother=baseCell(mother)
        self.rad=rad
        self.timeToHatch=timeToHatch
        self.Player=Player
    def Hatch(self): ##returns new cell to add ##
        if self.Player: ##Player cell egg hatching
            newCell = baseCell(self.mixPlayerCells(self.father,self.mother))
            newCell.location=Location(self.location.x, self.location.y)
            newCell=self.mutateCell(newCell,True)
            advance=self.chooseCell(newCell)
            newCell.randomStart=randint(0,10000)
            return advance,newCell
        else: #normal cell hatching
            newCell = baseCell(self.mixNormalCells(self.father,self.mother))
            newCell.location=Location(self.location.x, self.location.y)
            newCell=self.mutateCell(newCell)
            newCell.randomStart=randint(0,10000)
            return newCell
    def chooseCell(self,newCell):
        newtext=""
        for line in newCell.getAtts():
            newtext+=line+"\n"
        choice=easygui.boolbox(newtext,"Advance to this Cell?",["Yes","No"])
        if choice==0:
            return False
        return True
    def mutateCell(self,cell,Player=False):
        mutationchance=50
        goodbadchance=50
        mutationscale=[1,1,1,1,1,1,1,1,1,50,1,1,1,1,1,1] ##how much to mutate in every cell
        attIgnoreList=[0,4,6,7,11,12,16,17,18,19] ##what not to mutate

        for i in xrange(0,len(cell.getAtts())):
            if i in attIgnoreList:
                continue
            randchance=randint(0,100)
            if randchance<mutationchance: ##mutate attribute
                if randint(0,100)<goodbadchance: #bad or good mutation
                    mutationscale[i]*=-1

                if i==0: ##angle
                    cell.angle+=mutationscale[i]
                    text=str(cell.ID)+" mutated angle"
                    if Player:
                        easygui.msgbox(text)
                    else:
                        print text
                elif i==1: ##timeToLay+left
                    cell.timeToLay+=mutationscale[i]
                    cell.angle+=mutationscale[i]
                    text=str(cell.ID)+" mutated Timetolay"
                    if Player:
                        easygui.msgbox(text)
                    else:
                        print text
                elif i==2: ##eggWithdraw
                    cell.eggwithdraw+=mutationscale[i]
                    cell.angle+=mutationscale[i]
                    text=str(cell.ID)+" mutated eggWithdraw"
                    if Player:
                        easygui.msgbox(text)
                    else:
                        print text
                elif i==3: ##carnivore
                    cell.carnivore+=mutationscale[i]
                    cell.angle+=mutationscale[i]
                    text=str(cell.ID)+" mutated carnivore"
                    if Player:
                        easygui.msgbox(text)
                    else:
                        print text
                elif i==4: ##food
                    cell.food+=mutationscale[i]
                    cell.angle+=mutationscale[i]
                    text=str(cell.ID)+" mutated food"
                    if Player:
                        easygui.msgbox(text)
                    else:
                        print text
                elif i==5: ##foodWithdraw
                    cell.foodWithdraw+=mutationscale[i]
                    cell.angle+=mutationscale[i]
                    text=str(cell.ID)+" mutated foodWithdraw"
                    if Player:
                        easygui.msgbox(text)
                    else:
                        print text
                elif i==6: ##ID
                    cell.ID+=mutationscale[i]
                    cell.angle+=mutationscale[i]
                    text=str(cell.ID)+" mutated ID"
                    if Player:
                        easygui.msgbox(text)
                    else:
                        print text
                elif i==7: ##lastmother
                    cell.lastmother+=mutationscale[i]
                    cell.angle+=mutationscale[i]
                    text=str(cell.ID)+" mutated lastmother"
                    if Player:
                        easygui.msgbox(text)
                    else:
                        print text
                elif i==8: ##lifetime
                    cell.lifeTime+=mutationscale[i]
                    cell.angle+=mutationscale[i]
                    text=str(cell.ID)+" mutated lifetime"
                    if Player:
                        easygui.msgbox(text)
                    else:
                        print text
                elif i==9: ##lifetimeWithdraw
                    cell.lifewithdraw+=mutationscale[i]
                    cell.angle+=mutationscale[i]
                    text=str(cell.ID)+" mutated lifetimeWithdraw"
                    if Player:
                        easygui.msgbox(text)
                    else:
                        print text
                elif i==10: ##speed
                    cell.speed+=mutationscale[i]
                    cell.angle+=mutationscale[i]
                    text=str(cell.ID)+" mutated speed"
                    if Player:
                        easygui.msgbox(text)
                    else:
                        print text
                elif i==11: ##location
                    cell.location+=mutationscale[i]
                    cell.angle+=mutationscale[i]
                    text=str(cell.ID)+" mutated location"
                    if Player:
                        easygui.msgbox(text)
                    else:
                        print text
                elif i==12: ##rad
                    cell.rad+=mutationscale[i]
                    cell.angle+=mutationscale[i]
                    text=str(cell.ID)+" mutated rad"
                    if Player:
                        easygui.msgbox(text)
                    else:
                        print text
                elif i==13: ##ai
                    cell.AI+=mutationscale[i]
                    cell.angle+=mutationscale[i]
                    text=str(cell.ID)+" mutated AI"
                    if Player:
                        easygui.msgbox(text)
                    else:
                        print text
                elif i==14: ##vision
                    cell.vision+=mutationscale[i]
                    cell.angle+=mutationscale[i]
                    text=str(cell.ID)+" mutated vision"
                    if Player:
                        easygui.msgbox(text)
                    else:
                        print text
                elif i==15: ##eggHatchTime
                    cell.eggHatchTime+=mutationscale[i]
                    cell.angle+=mutationscale[i]
                    text=str(cell.ID)+" mutated eggHatchTime"
                    if Player:
                        easygui.msgbox(text)
                    else:
                        print text
        return cell
    def mixPlayerCells(self,mother,father):
        if easygui.buttonbox("Manual or Auto?","",["Manual","Auto"])=="Auto":
            return self.mixNormalCells(mother,father)
        else: ## manual mode
            attIgnoreList=[0,4,6,7,11,12,16,17,18,19]
            print "\n\n"
            print "mixing cells manual"
            newCell=baseCell(father)
            for i in xrange(0,len(father.getAtts())):
                if i in attIgnoreList:
                    continue
                ##print colored("(1)","blue"), colored(father.getAtts()[i].ljust(25),"magenta"),
                ##print colored("(2)","blue"), colored(mother.getAtts()[i],"magenta")
                ##choice=raw_input()
                fathertext=father.getAtts()[i]
                mothertext=mother.getAtts()[i]
                choice=easygui.buttonbox("Choose attribute:","",[fathertext,mothertext])

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
                    if choice==fathertext:
                        newCell.food=father.food
                    else:
                        newCell.food=mother.food
                elif i==5: ##foodWithdraw
                    if choice==fathertext:
                        newCell.foodWithdraw=father.foodWithdraw
                    else:
                        newCell.foodWithdraw=mother.foodWithdraw
                elif i==6: ##ID
                    if choice==fathertext:
                        newCell.ID=father.ID
                    else:
                        newCell.ID=mother.ID
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
        return newCell
    def mixNormalCells(self,mother,father):
        attIgnoreList=[0,4,6,7,11,12,16,17,18,19]
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
                if choice==fathertext:
                    newCell.food=father.food
                else:
                    newCell.food=mother.food
            elif i==5: ##foodWithdraw
                if choice==fathertext:
                    newCell.foodWithdraw=father.foodWithdraw
                else:
                    newCell.foodWithdraw=mother.foodWithdraw
            elif i==6: ##ID
                if choice==fathertext:
                    newCell.ID=father.ID
                else:
                    newCell.ID=mother.ID
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
        return newCell
    def consumeHatch(self,counter):
        if not self.timeToHatch==0: #egg is hatching
            if counter%pyEvoMain.framerate==0:
                self.timeToHatch-=1
class AbCell:
    target=None
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
    dead=False
    eggHatchTime=0
    randomStart=0
    def checkEat(self,foodList):
            for food in foodList:
                if math.sqrt(((self.location.x-food.location.x)**2)+((self.location.y-food.location.y)**2))<self.rad+food.rad:
                    self.eat(food)
                    foodList.remove(food)
    def changeAngle(self, dir):
        self.angle=(self.angle+dir)%8 ##0 is up, clockwise (2 is right)
    def eat(self, food):
        self.foodLeft+=food.getAmount()
        print self.ID, "ate food"
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
        list.append("AI: "+str(self.AI))
        list.append("vision: "+str(self.vision))
        list.append("eggHatchTime: "+str(self.eggHatchTime))
        list.append(" ")
        list.append("foodLeft: "+str(self.foodLeft))
        list.append("lifeTimeLeft: "+str(self.lifeTimeLeft))
        list.append("mode : "+str(self.mode))
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
    def __init__(self,cell=None,angle=None,carnivore=None,eggwithdraw=None,foodLeft=None,foodWithdraw=None,ID=None,lifeTime=None,location=None,speed=None,rad=None,lifewithdraw=None,timeToLay=None,AI=None,vision=None,eggHatchTime=None):
        if cell==None:
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
            self.ID=algorithm.getNextID()
            self.rad=rad
            self.lifeTime=lifeTime
            self.lifeTimeLeft=lifeTime
            self.location=Location(location.x,location.y)
            self.speed=speed
            self.eggHatchTime=eggHatchTime
            self.mode='m'
            self.lastMother=self
            self.randomStart=randint(0,10000)
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
            self.foodLeft=cell.food
            self.foodWithdraw=cell.foodWithdraw
            self.ID=algorithm.getNextID()
            self.rad=cell.rad
            self.lifeTime=cell.lifeTime
            self.lifeTimeLeft=cell.lifeTime
            self.location=Location(cell.location.x,cell.location.y)
            self.speed=cell.speed
            self.eggHatchTime=cell.eggHatchTime
            self.mode='m'
            self.lastMother=cell.lastMother
            self.randomStart=cell.randomStart