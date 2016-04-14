__author__ = 'user-pc'
import pygame
import graphics
import classes
import consts
import random
import math
import AI
import pickle
from os import path
practicle_radius=12
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
    def __init__(self,height,width): #temp
        if consts.loadedGame==False: ##new game ##change true to 'consts.loadedGame==False'
            ##(cell,angle,carnivore,eggwithdraw,food,foodWithdraw,ID,lifeTime,location,speed,rad,lifewithdraw,timeToLay,AI,vision,eggHatchTime,strength=0):
            self.screenheight=height
            self.screenwidth=width
            angle=4
            lifewithdraw=consts.framerate
            carnivore=0
            eggwithdraw=consts.framerate
            food=15
            foodWithdraw=consts.framerate
            rad=10
            AI=2
            vision=500
            lifeTime=20
            p_lifetime=lifeTime
            p_food=food
            speed=1
            timeToLay=10
            eggHatchTime=3
            strength=5
            #                            cell,angle,carnivore,eggwithdraw,foodleft,foodwithdraw,ID,Lifetime,location,speed,rad,lifewithdeaw,timetolay,AI,vision,eggHatchtime,strngth
            self.myCell=classes.baseCell(None,angle,carnivore,eggwithdraw,p_food,foodWithdraw,0,p_lifetime,classes.Location(400,400),speed,rad,lifewithdraw,timeToLay,AI,vision,eggHatchTime,strength)
            self.myCell.base90, self.myCell.base45 = pygame.image.load('src/IMG/HeadD.png'),pygame.image.load('src/IMG/HeadUL.png')
            self.myCell.image=self.myCell.base90
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
            ##self.cellEggs[0].mixPlayerCells(self.myCell,self.myCell)
            ##self.cellEggs.append(classes.Egg((100,100),self.cellList[0],None,6,0))
            self.putFood()
        else: ##later code goes here
            file_path = path.relpath("src/SAV/foodList.sav")
            file = open(file_path,"r")
            sp=file.read().split('\n')
            self.load(sp)
            file.close()
            self.myCell.base90, self.myCell.base45 = pygame.image.load('src/IMG/HeadD.png'),pygame.image.load('src/IMG/HeadUL.png')
            self.myCell.image=self.myCell.base90

    def putFood(self):
        self.foodList.append(classes.Food(classes.Location(random.randint(0,consts.screenwidth),random.randint(0,consts.screenheight)),1,5))
    def growCellEggs(self):
        for egg in self.cellEggs:
            if egg.timeToHatch==0:
                newCell=egg.Hatch()
                self.cellList.append(newCell)
                self.cellEggs.remove(egg)
                ##egg hatch practicle
                graphics.practicleList.append(classes.practicle(egg.location,(163,213,230),practicle_radius))
    def growPlayerEggs(self):
        for egg in self.myEggs:
            if egg.timeToHatch==0:
                advance,newCell=egg.Hatch()
                if advance:
                    self.myCell.base90, self.myCell.base45 = pygame.image.load('src/IMG/e_HeadD.png'),pygame.image.load('src/IMG/e_HeadUL.png')
                    self.myCell.image=self.myCell.base90

                    self.cellList.append(self.myCell)
                    self.myEggs.remove(egg)
                    self.myCell=newCell

                    self.myCell.base90, self.myCell.base45 = pygame.image.load('src/IMG/HeadD.png'),pygame.image.load('src/IMG/HeadUL.png')
                    self.myCell.image=self.myCell.base90
                else:
                    self.cellList.append(newCell)
                    self.myEggs.remove(egg)
                ##egg hatch practicle
                graphics.practicleList.append(classes.practicle(egg.location,(163,213,230),practicle_radius))
    def getInput(self):
        returnList=[]
        events = pygame.event.get(pygame.KEYDOWN)
        if consts.mouse_control:#mouse control
            angle=0
            x1=self.myCell.location.x
            y1=self.myCell.location.y
            x2=pygame.mouse.get_pos()[0]
            y2=pygame.mouse.get_pos()[1]
            dx=x2-x1
            if  not dx==0:
                dy=y2-y1
                ##print("dx: " + str(dx) + " dy: " + str(dy))
                calc_angle= (math.atan(dy/dx) * -180 / math.pi)
                print "calc angle: ", calc_angle
                if (-22.5<calc_angle<=22.5) and (dx>0): ##Right
                    angle = 2
                elif (22.5<calc_angle<=67.5) and (dx>0): ##Right Up
                    angle = 1
                elif (67.5<calc_angle<=90) and (dx>0): ##Up
                    angle = 0
                elif (-90<calc_angle<=-67.5) and (dx<0): ##Up
                    angle = 0
                elif (-67.5<calc_angle<=-22.5) and (dx<0): ##Left Up
                    angle = 7
                elif (-22.5<calc_angle<=22.5) and (dx<0): ##Left
                    angle = 6
                elif (22.5<calc_angle<=67.5) and (dx<0): ##Left Down
                    angle = 5
                elif (67.5<calc_angle<=90) and (dx<0): ##Down
                    angle = 4
                elif (-90<calc_angle<=-67.5) and (dx>0): ##Down
                    angle = 4
                elif (-67.5<calc_angle<=-22.5) and (dx>0): ##Right Down
                    angle = 3
                self.myCell.angle=angle
        for event in events:
            if not consts.mouse_control: #keyboard
                if event.key==pygame.K_LEFT:
                    returnList.append("Left")
                    self.__lastTimeSinceKey["Left"]=0
                if event.key==pygame.K_RIGHT:
                    returnList.append("Right")
                    self.__lastTimeSinceKey["Right"]=0


            if event.key==pygame.K_a:
                returnList.append("a")
            if event.key==pygame.K_m:
                returnList.append("m")
            if event.key==pygame.K_c:
                returnList.append("c")
            if event.key==pygame.K_p:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
        key=pygame.key.get_pressed()
        #check for hold
        if key[pygame.K_LEFT]:
            if self.__lastTimeSinceKey["Left"]>consts.framerate/17:
                returnList.append("OLeft")
                self.__lastTimeSinceKey["Left"]=0
            else:
                self.__lastTimeSinceKey["Left"]+=1
        if key[pygame.K_RIGHT]:
            if self.__lastTimeSinceKey["Right"]>consts.framerate/17:
                returnList.append("ORight")
                self.__lastTimeSinceKey["Right"]=0
            else:
                self.__lastTimeSinceKey["Right"]+=1
        #check up and down
        if not consts.mouse_control: #keyboard
            if key[pygame.K_UP]:
                returnList.append("Up")
            return returnList
        else: #mouse
            if (pygame.mouse.get_pressed()[0]):
                returnList.append("Up")
            return returnList

    def save(self):
        dt=""
        for food in self.foodList:
            dt+="F|"
            dt+=str(food.location.x)+"|"
            dt+=str(food.location.y)+"|"
            dt+=str(food.amount)+"|"
            dt+="\n"
        for egg in self.cellEggs:
            dt+="EC|"
            dt+=str(egg.location.x)+"|"
            dt+=str(egg.location.y)+"|"
            dt+=str(egg.father)+"|"
            dt+=str(egg.mother)+"|"
            dt+=str(egg.timeToHatch)+"|"
            dt+="\n"
        for egg in self.myEggs:
            dt+="EP|"
            dt+=str(egg.location.x)+"|"
            dt+=str(egg.location.y)+"|"
            dt+=str(egg.father)+"|"
            dt+=str(egg.mother)+"|"
            dt+=str(egg.timeToHatch)+"|"
            dt+="\n"
        #self,cell,angle,carnivore,eggwithdraw,foodLeft,foodWithdraw,ID,lifeTime,location,speed,rad,lifewithdraw,timeToLay,AI,vision,eggHatchTime,strength=0):
        for cell in self.cellList:
            dt+="C|"#0
            dt+=str(cell.location.x)+"|"#1
            dt+=str(cell.location.y)+"|"#2
            dt+=str(cell.angle)+"|"#3
            dt+=str(cell.carnivore)+"|"
            dt+=str(cell.eggwithdraw)+"|"
            dt+=str(cell.foodLeft)+"|"
            dt+=str(cell.foodWithdraw)+"|"
            dt+=str(cell.ID)+"|"
            dt+=str(cell.lifeTime)+"|"
            dt+=str(cell.speed)+"|"
            dt+=str(cell.lifewithdraw)+"|"
            dt+=str(cell.timeToLay)+"|"
            dt+=str(cell.AI)+"|"
            dt+=str(cell.vision)+"|"
            dt+=str(cell.eggHatchTime)+"|"
            dt+=str(cell.strength)+"|"
            dt+="\n"
        dt+="CP|"#0
        dt+=str(self.myCell.location.x)+"|"#1
        dt+=str(self.myCell.location.y)+"|"#2
        dt+=str(self.myCell.angle)+"|"#3
        dt+=str(self.myCell.carnivore)+"|"
        dt+=str(self.myCell.eggwithdraw)+"|"
        dt+=str(self.myCell.foodLeft)+"|"
        dt+=str(self.myCell.foodWithdraw)+"|"
        dt+=str(self.myCell.ID)+"|"
        dt+=str(self.myCell.lifeTime)+"|"
        dt+=str(self.myCell.speed)+"|"
        dt+=str(self.myCell.lifewithdraw)+"|"
        dt+=str(self.myCell.timeToLay)+"|"
        dt+=str(self.myCell.AI)+"|"
        dt+=str(self.myCell.vision)+"|"
        dt+=str(self.myCell.eggHatchTime)+"|"
        dt+=str(self.myCell.strength)+"|"
        dt+="\n"

        dt+="T|"+str(consts.counter/consts.framerate)+"\n"
        return dt
    def load(self,sp):
        for object in sp:
            if object=="":
                break
            spp=object.split('|')
            if spp[0]=="F":
                self.foodList.append(classes.Food(classes.Location(int(spp[1]),int(spp[2])),int(spp[3]),5))
            if spp[0]=="EC":
                self.cellEggs.append(classes.Egg(classes.Location(int(spp[1]),int(spp[2])),int(spp[3]),int(spp[4]),6,int(spp[5]),False))
            if spp[0]=="EP":
                self.cellEggs.append(classes.Egg(classes.Location(int(spp[1]),int(spp[2])),int(spp[3]),int(spp[4]),6,int(spp[5]),True))
            if spp[0]=="C":
                #self,cell,angle,carnivore,eggwithdraw,foodLeft,foodWithdraw,ID,lifeTime,location,speed,rad,lifewithdraw,timeToLay,AI,vision,eggHatchTime,strength=0):
                self.cellList.append(classes.baseCell(None,int(spp[3]),int(spp[4]),int(spp[5]),int(spp[6]),int(spp[7]),int(spp[8]),int(spp[9]),classes.Location(int(spp[1]),int(spp[2])),int(spp[10]),10,int(spp[11]),int(spp[12]),int(spp[13]),int(spp[14]),int(spp[15]),int(spp[16])))
            if spp[0]=="CP":
                self.myCell=classes.baseCell(None,int(spp[3]),int(spp[4]),int(spp[5]),int(spp[6]),int(spp[7]),int(spp[8]),int(spp[9]),classes.Location(int(spp[1]),int(spp[2])),int(spp[10]),10,int(spp[11]),int(spp[12]),int(spp[13]),int(spp[14]),int(spp[15]),int(spp[16]))
            if spp[0]=="T":
                consts.counter=int(spp[1])*consts.framerate
                self._counter=int(spp[1])*consts.framerate
    def LoadSaveMenu(self):
        choice=None
        while choice not in ["Save and Quit","Resume"]:
            choice=graphics.askBoard("manual","Game Paused","Save and Quit","Resume")
        if choice=="Save and Quit":
            file_path = path.relpath("src/SAV/foodList.sav")
            file = open(file_path,"wb")
            file.write(self.save())
            file.close()
            pygame.event.post(pygame.event.Event(pygame.QUIT))
    def nextStep(self,text):
        if consts.godmode:
            self.myCell.lifeTimeLeft=self.myCell.lifeTime
            self.myCell.foodLeft=self.myCell.food
        if text!="Empty":
            consts.askingQuestion=False
            ##parse input
        self._counter+=1

        ##change season

        if not consts.recording:
            if self._counter%(consts.framerate*60)==0:
                consts.season=(consts.season+1)%4
        ##handle input
        inputlist=self.getInput()
        for item in inputlist:
            if (item=="Left" or item=="Right") and (("Left" in self.__kinput) or ("Right" in self.__kinput)):
                continue
            elif (item=="c" and ("c" in self.__kinput)):
                continue
            elif (item=="m" and ("m" in self.__kinput)):
                continue
            else:
                self.__kinput.append(item)
        for item in self.__kinput:
            if not consts.mouse_control:
                if item=="Left" or item=="OLeft":
                    self.myCell.changeAngle(-1)
                if item=="Right" or item=="ORight":
                    self.myCell.changeAngle(1)
        self.myCell.changeAngle(0)
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
                if "Up" == item:
                    cell.move()
                if "a" == item:
                    if cell.timeToLayLeft==0 and cell.lastMother!=None:
                        self.cellEggs.append(cell.layEgg())
                        cell.lastMother=None
                        cell.target=None
                if "c" ==item:
                    if cell.mode=="m":
                        cell.mode="c"
                    else:
                        cell.mode="m"

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
            if self.myCell.timeToLayLeft==0 and self.myCell.lastMother!=None:
                self.myEggs.append(self.myCell.layEgg(True))
                self.myCell.lastMother=None

        if "c" in inputlist: ##carnivore or mating
            if self.myCell.mode=='m':
                self.myCell.mode='c'
            else:
                self.myCell.mode='m'
        if "m" in inputlist: ##load/save menu
            self.LoadSaveMenu()
        ##check egg hatching
        for egg in self.cellEggs:
            egg.consumeHatch(self._counter)
        for egg in self.myEggs:
            egg.consumeHatch(self._counter)
        self.growCellEggs()
        self.growPlayerEggs()



        ##check for carnivore eating and mating
        allCells=[]
        noCollision=True
        for cell in self.cellList:
            allCells.append(cell)
        allCells.append(self.myCell)
        for cell in allCells:
            for otherCell in allCells:
                collision=math.sqrt(((cell.location.x-otherCell.location.x)**2)+((cell.location.y-otherCell.location.y)**2))<cell.rad+otherCell.rad
                if (cell.ID!=otherCell.ID) and (collision): ##not the same cell
                    noCollision=False
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
                            ##cell eat practicle
                            if cell.lastCollision!=otherCell and otherCell.lastCollision!=cell: ##only if its not a false collision
                                graphics.practicleList.append(classes.practicle(cell.location,(240,165,36),practicle_radius))
                                cell.lastCollision=otherCell
                    if cell.mode=='m': ##mate
                        if otherCell.mode=='m': ##mate too
                            cell.lastMother=otherCell
                            otherCell.lastMother=cell
                            ##cell eat practicle
                            if cell.lastCollision!=otherCell and otherCell.lastCollision!=cell: ##only if its not a false collision
                                graphics.practicleList.append(classes.practicle(cell.location,(240,36,131),practicle_radius))
                                cell.lastCollision=otherCell
            if noCollision: ##the cell has not colided, reset the last collision
                cell.lastCollision=cell.ID+self._counter



        #grow more food
        """
        0-Summer 75%
        1-Autumn 50%
        2-winter 25%
        3-spring 100%
        """

        if consts.season==0:
            if self._counter%(consts.framerate/6)==0:
                self.putFood()
        elif consts.season==1:
            if self._counter%(consts.framerate/4)==0:
                self.putFood()
        elif consts.season==2:
            if self._counter%(consts.framerate/2)==0:
                self.putFood()
        elif consts.season==3:
            if self._counter%(consts.framerate/8)==0:
                self.putFood()

        consts.counter=self._counter
        self.__kinput=[]

        if self.myCell.dead:
            choice=None
            while choice!="Okay":
                choice = graphics.askBoard("Prompt","You have died :(\n\nYou lived " + str(consts.counter/consts.framerate)+" seconds.")
            pygame.event.post(pygame.event.Event(pygame.QUIT))

        ##deduct practicle time
        if (self._counter%(consts.framerate*0.125)):
            for practicle in graphics.practicleList:
                if practicle.radius==1:
                    graphics.practicleList.remove(practicle)
                else:
                    practicle.radius-=1