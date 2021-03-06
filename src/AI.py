__author__ = 'user-pc'
import pygame
import graphics
import classes
import random
import math
import consts

"""
ai0=random and not moving while rotating
ai1=random movement
ai2=random food,random mate,doesnt move across
ai3=closest food,closest mate,doesnt move across
ai4-closest food,best mate,does move across
"""
def nextStep(playerCell,cellList,foodList,currCell):
    foodsee=[]
    cellsee=[]
    foodsee,cellsee=look4Food(currCell,foodList,cellList,playerCell)
    input1=[]
    if currCell.AI==0:
        input1=AI0(currCell)
    elif currCell.AI==1:
        input1=AI1(currCell)
    elif currCell.AI==2:
        input1=AI2(currCell,foodsee,cellsee)
    elif currCell.AI==3:
        input1=AI3(currCell,foodsee,cellsee)
    elif currCell.AI>=4:
        input1=AI4(currCell,foodsee,cellsee)
    elif currCell.AI==-1: ## dont move for debug purposes
        input1 = []
    return input1

def look4Food(cell,foodList,cellList,playerCell):
    foodsee=[]
    cellsee=[]
    for food in foodList:
        if math.sqrt(((cell.location.x-food.location.x)**2)+((cell.location.y-food.location.y)**2))<cell.vision and insideCircle(food):
            foodsee.append(food)
    for curr in cellList:
        if math.sqrt(((cell.location.x-curr.location.x)**2)+((cell.location.y-curr.location.y)**2))<cell.vision and insideCircle(curr):
            cellsee.append(curr)
    if math.sqrt(((cell.location.x-playerCell.location.x)**2)+((cell.location.y-playerCell.location.y)**2))<cell.vision and insideCircle(playerCell):
        cellsee.append(playerCell)
    if cell in cellsee:
        cellsee.remove(cell)
    return foodsee,cellsee
def AI0(cell):
    input=[]
    ##lay egg if possible
    if cell.timeToLayLeft==0:
        input.append("a")

    i=random.randint(0,50)
    if i==0:
        input.append("ORight")
    if i==1:
        input.append("OLeft")
    if 1<i<10:
        input.append("Up")
    return input
def AI1(cell):
    input=[]
    ##lay egg if possible
    if cell.timeToLayLeft==0:
        input.append("a")

    i=random.randint(0,50)
    if i==0:
        input.append("ORight")
    if i==1:
        input.append("OLeft")
    input.append("Up")
    return input
def AIM(cell,foodList,cellList,findFunc,GoFunc,findMateFunc):
    input = []
    if (cell.target not in foodList) and (cell.target not in cellList):
        cell.target = None
    if not insideCircle(cell.target):
        cell.target = None
    if kindOfTheSame(math.sqrt(((cell.location.x - consts.screenwidth / 2) ** 2) + ((cell.location.y - consts.screenheight / 2) ** 2)), consts.p2radius) or not insideCircle(cell):
        cell.bugMode = "EscapingCircle"
        input = GoFunc(cell, consts.center)
        return input
    if cell.lastMother != None:
        if cell.lastMotherHelper == None:  # just mate
            cell.target = None
            cell.lastMotherHelper = cell.lastMother
    else:
        cell.lastMotherHelper = None
    if cell.timeToLayLeft <= cell.timeToLay / 3 and cell.lastMother == None and len(cellList) != 0:
        cell.bugMode = "Look4Mate"
        if not validMate(cell.target):
            target = findMateFunc(cell, cellList)
            if target!=None:
                cell.target=target
        if cell.target != None:
            input = GoFunc(cell, cell.target)
            if cell.mode != "m":
                input.append("c")
        if len(input) != 0:
            return input
    ##search food
    a = 0
    if cell.target == None:
        if cell.carnivore == 1:
            a = random.randint(0, 1)
            if a == 1:  # vegan food
                cell.bugMode = "Look4veganFoodAndCar"
                if len(foodList) == 0:
                    input = AI1(cell)
                    return input
                cell.target = findFunc(cell, foodList)
                if cell.target != None:
                    input = GoFunc(cell, cell.target)
                else:
                    input = AI1(cell)
            elif len(cellList) != 1:  # real food
                cell.bugMode = "Look4RealFood"
                if len(cellList) == 1:
                    input = AI1(cell)
                    return input
                cell.target = findFunc(cell, cellList)
                if cell.target != None:
                    input = GoFunc(cell, cell.target)
                    if cell.mode != "c":
                        input.append("c")
                else:
                    input = AI1(cell)
        else:
            cell.bugMode = "Look4veganFood"
            if len(foodList) == 0:
                input = AI1(cell)
                return input
            cell.target = findFunc(cell, foodList)
            if cell.target != None:
                input = GoFunc(cell, cell.target)
            else:
                input = AI1(cell)
    else:
        cell.bugMode = "OnMyWay"
        input = GoFunc(cell, cell.target)
    if cell.timeToLayLeft == 0 and cell.lastMother != None:  ##lay egg if possible
        input.append("a")
    return input
#DONE
def findRandomMate(cell,cellList):
    i = random.randint(0, len(cellList) - 1)
    j = len(cellList) * 5
    while cellList[i].mode == "c":
        if j == 0:
            j = -1
            break
        i = random.randint(0, len(cellList) - 1)
        j -= 1
    if j != -1:
        return cellList[i]
    else:
        return None
#DONE
def findRandomFood(cell,foodList):
    if len(foodList)==0:
        return None
    else:
        return foodList[random.randint(0,len(foodList)-1)]
def AI2(cell,foodList,cellList):
    """
    input=[]
    ##check for circle
    j=0
    if (cell.target not in foodList) and (cell.target not in cellList):
        cell.target=None
    if not insideCircle(cell.target):
        cell.target=None
    if kindOfTheSame(math.sqrt(((cell.location.x-consts.screenwidth/2)**2)+((cell.location.y-consts.screenheight/2)**2)),consts.p2radius) or math.sqrt(((cell.location.x-consts.screenwidth/2)**2)+((cell.location.y-consts.screenheight/2)**2))>consts.p2radius:
        cell.bugMode = "EscapingCircle"
        input=goto(cell,consts.center)
        return input
    ##search mate if its mating time
    if cell.lastMother!=None:
        if cell.lastMotherHelper==None:#just mate
            cell.target=None
            cell.lastMotherHelper=cell.lastMother
    else:
        cell.lastMotherHelper = None
    if cell.timeToLayLeft<=cell.timeToLay/3 and cell.lastMother==None and len(cellList)!=0:
        cell.bugMode="Look4Mate"
        if not validMate(cell.target):
            i=random.randint(0,len(cellList)-1)
            j=len(cellList)*5
            while cellList[i].ID==cell.ID or not insideCircle(cellList[i]) or cellList[i].mode=="c":
                if j == 0:
                    j=-1
                    break
                i=random.randint(0,len(cellList)-1)
                j -= 1
            if j!=-1:
                cell.target=cellList[i]
        if cell.target!=None and j!=-1:
            input=goto(cell,cell.target)
            if cell.mode!="m":
                input.append("c")
        if len(input)!=0:
            return input
    ##search food
    a=0
    if cell.target==None:
        if cell.carnivore==1:
            a=random.randint(0,1)
            if a==1:#vegan food
                cell.bugMode = "Look4veganFoodAndCar"
                if len(foodList) == 0:
                    input = AI1(cell)
                    return input
                j=len(foodList)*5
                while cell.target==None or not insideCircle(cell.target):
                    if j == 0:
                        cell.target = None
                        j=-1
                        break
                    j-=1
                    i = random.randint(0, len(foodList) - 1)
                    cell.target=foodList[i]
                if cell.target!=None:
                    input=goto(cell,cell.target)
                else:
                    input = AI1(cell)
            elif len(cellList)!=1:#real food
                cell.bugMode = "Look4RealFood"
                if len(cellList) == 1:
                    input = AI1(cell)
                    return input
                j = len(cellList) * 5
                while cell.target == None or not insideCircle(cell.target):
                    if j == 0:
                        cell.target = None
                        j=-1
                        break
                    i = random.randint(0, len(cellList) - 1)
                    cell.target = cellList[i]
                    j -= 1
                if cell.target != None:
                    input = goto(cell, cell.target)
                    if cell.mode!="c":
                        input.append("c")
                else:
                    input = AI1(cell)
        else:
            cell.bugMode = "Look4veganFood"
            if len(foodList) == 0:
                input = AI1(cell)
                return input
            j = len(foodList) * 5
            while cell.target == None or not insideCircle(cell.target):
                if j == 0:
                    cell.target = None
                    j = -1
                    break
                j -= 1
                i = random.randint(0, len(foodList) - 1)
                cell.target = foodList[i]
            if cell.target != None:
                input = goto(cell, cell.target)
            else:
                input = AI1(cell)
    else:
        cell.bugMode = "OnMyWay"
        input = goto(cell, cell.target)
    if cell.timeToLayLeft==0 and cell.lastMother!=None:##lay egg if possible
            input.append("a")
    return input
    """
    return AIM(cell,foodList,cellList,findRandomFood,goto,findRandomMate)
def AI3(cell,foodList,cellList):
    """
    input=[]
    if (cell.target not in foodList) and (cell.target not in cellList):
        cell.target = None
    if not insideCircle(cell.target):
        cell.target = None
    if kindOfTheSame(math.sqrt(((cell.location.x - consts.screenwidth / 2) ** 2) + (
        (cell.location.y - consts.screenheight / 2) ** 2)), consts.p2radius) or math.sqrt(
                    ((cell.location.x - consts.screenwidth / 2) ** 2) + (
                (cell.location.y - consts.screenheight / 2) ** 2)) > consts.p2radius:
        cell.bugMode = "EscapingCircle"
        input = goto(cell, consts.center)
        return input
    if cell.lastMother != None:
        if cell.lastMotherHelper == None:  # just mate
            cell.target = None
            cell.lastMotherHelper = cell.lastMother
    else:
        cell.lastMotherHelper = None
    if cell.timeToLayLeft<=cell.timeToLay/3 and cell.lastMother==None and len(cellList)!=1 :
        cell.bugMode = "Look4Mate"
        cell.target=None
        cell.target=closestMate(cell,cellList)
        if cell.target!=None:
            input=goto(cell,cell.target)
            if cell.mode!="m":
                input.append("c")
        if len(input) != 0:
            return input
    ##search food
    a = 0
    if cell.target == None:
        if cell.carnivore == 1:
            a = random.randint(0, 1)
            if a == 1:  # vegan food
                cell.bugMode = "Look4veganFoodAndCar"
                if len(foodList) == 0:
                    input = AI1(cell)
                    return input
                cell.target = closestFood(cell,foodList)
                if cell.target != None:
                    input = goto(cell, cell.target)
                else:
                    input = AI1(cell)
            elif len(cellList) != 1:  # real food
                cell.bugMode = "Look4RealFood"
                if len(cellList) == 1:
                    input = AI1(cell)
                    return input
                cell.target = closestFood(cell,cellList)
                if cell.target != None:
                    input = goto(cell, cell.target)
                    if cell.mode != "c":
                        input.append("c")
                else:
                    input = AI1(cell)
        else:
            cell.bugMode = "Look4veganFood"
            if len(foodList) == 0:
                input = AI1(cell)
                return input
            cell.target = closestFood(cell, foodList)
            if cell.target != None:
                input = goto(cell, cell.target)
            else:
                input = AI1(cell)
    else:
        cell.bugMode = "OnMyWay"
        input = goto(cell, cell.target)
    if cell.timeToLayLeft == 0 and cell.lastMother != None:  ##lay egg if possible
        input.append("a")
    return input
    """
    return AIM(cell,foodList,cellList,closestFood,goto,closestMate)
def AI4(cell,foodList,cellList):
    """
    input = []
    if (cell.target not in foodList) and (cell.target not in cellList):
        cell.target = None
    if not insideCircle(cell.target):
        cell.target = None
    if kindOfTheSame(math.sqrt(((cell.location.x - consts.screenwidth / 2) ** 2) + (
                (cell.location.y - consts.screenheight / 2) ** 2)), consts.p2radius) or math.sqrt(
                ((cell.location.x - consts.screenwidth / 2) ** 2) + (
                    (cell.location.y - consts.screenheight / 2) ** 2)) > consts.p2radius:
        cell.bugMode = "EscapingCircle"
        input = goodGoTo(cell, consts.center)
        return input
    if cell.lastMother != None:
        if cell.lastMotherHelper == None:  # just mate
            cell.target = None
            cell.lastMotherHelper = cell.lastMother
    else:
        cell.lastMotherHelper = None
    if cell.timeToLayLeft <= cell.timeToLay / 3 and cell.lastMother == None and len(cellList) != 1:
        cell.bugMode = "Look4Mate"
        cell.target = None
        cell.target = bestMate(cell, cellList)
        if cell.target != None:
            input = goodGoTo(cell, cell.target)
            if cell.mode != "m":
                input.append("c")
        if len(input) != 0:
            return input
    ##search food
    a = 0
    if cell.target == None:
        if cell.carnivore == 1:
            a = random.randint(0, 1)
            if a == 1:  # vegan food
                cell.bugMode = "Look4veganFoodAndCar"
                if len(foodList) == 0:
                    input = AI1(cell)
                    return input
                cell.target = closestFood(cell, foodList)
                if cell.target != None:
                    input = goodGoTo(cell, cell.target)
                else:
                    input = AI1(cell)
            elif len(cellList) != 1:  # real food
                cell.bugMode = "Look4RealFood"
                if len(cellList) == 1:
                    input = AI1(cell)
                    return input
                cell.target = closestFood(cell, cellList)
                if cell.target != None:
                    input = goodGoTo(cell, cell.target)
                    if cell.mode != "c":
                        input.append("c")
                else:
                    input = AI1(cell)
        else:
            cell.bugMode = "Look4veganFood"
            if len(foodList) == 0:
                input = AI1(cell)
                return input
            cell.target = closestFood(cell, foodList)
            if cell.target != None:
                input = goodGoTo(cell, cell.target)
            else:
                input = AI1(cell)
    else:
        cell.bugMode = "OnMyWay"
        input = goodGoTo(cell, cell.target)
    if cell.timeToLayLeft == 0 and cell.lastMother != None:  ##lay egg if possible
        input.append("a")
    return input
    """
    return AIM(cell,foodList,cellList,closestFood,goodGoTo,bestMate)
#DONE
def insideCircle(object):
    if object==None:
        return False
    if math.sqrt(((object.location.x-consts.screenwidth/2)**2)+((object.location.y-consts.screenheight/2)**2))<consts.p2radius:
        return True
    else:
        return False
#DONE
def goto(cell,object):
    input = []
    direction=0
    if kindOfTheSame(cell.location.y, object.location.y):
        if cell.location.x > object.location.x:  # 6
            input = moveLeft(cell)
            return input
        if cell.location.x < object.location.x:  # 2
            input = moveRight(cell)
            return input
    elif cell.location.y < object.location.y:  # target is under cell
        if kindOfTheSame(cell.location.x, object.location.x):  # 4
            input = moveDown(cell)
            return input
        if cell.location.x > object.location.x:  # 5
            direction = 5
        if cell.location.x < object.location.x:  # 3
            direction = 3
    elif cell.location.y > object.location.y:  # target is above cell
        if kindOfTheSame(cell.location.x, object.location.x):  # 0
            input = moveUp(cell)
            return input
        if cell.location.x > object.location.x:  # 7
            direction = 7
        if cell.location.x < object.location.x:  # 1
            direction = 1
    if direction==1:
        if math.sqrt(((cell.location.x-consts.screenwidth/2)**2)+((object.location.y-consts.screenheight/2)**2))<consts.p2radius:
            if cell.location.y != object.location.y:  # check if same y if not move Up
                input = moveUp(cell)
            else:  # if yes move left
                input = moveRight(cell)
        else:#if the original route will pass outside the circle
            if cell.location.x != object.location.x:  # check if same x if not move Right
                input = moveRight(cell)
            else:  # if yes move Up
                input = moveUp(cell)
    if direction==3:
        if math.sqrt(((cell.location.x - consts.screenwidth / 2) ** 2) + (((object.location.y) - consts.screenheight / 2) ** 2)) < consts.p2radius:
            if cell.location.y != object.location.y:  # check if same y if not move down
                input = moveDown(cell)
            else:  # if yes move right
                input = moveRight(cell)
        else:
            if cell.location.x != object.location.x:  # check if same y if not move down
                input = moveRight(cell)
            else:  # if yes move right
                input = moveDown(cell)
    if direction==5:
        if math.sqrt(((cell.location.x - consts.screenwidth / 2) ** 2) + (
            ((object.location.y) - consts.screenheight / 2) ** 2)) < consts.p2radius:
            if cell.location.y != object.location.y:  # check if same y if not move down
                input = moveDown(cell)
            else:  # if yes move left
                input = moveLeft(cell)
        else:
            if cell.location.x != object.location.x:  # check if same y if not move down
                input = moveLeft(cell)
            else:  # if yes move left
                input = moveDown(cell)
    if direction == 7:
        if math.sqrt(((cell.location.x - consts.screenwidth / 2) ** 2) + (((object.location.y) - consts.screenheight / 2) ** 2)) < consts.p2radius:
            if cell.location.y != object.location.y:  # check if same y if not move down
                input = moveUp(cell)
            else:  # if yes move right
                input = moveLeft(cell)
        else:
            if cell.location.x != object.location.x:  # check if same y if not move down
                input = moveLeft(cell)
            else:  # if yes move right
                input = moveUp(cell)
    return input
#DONE
def goodGoTo(cell,object):
    input=[]
    if kindOfTheSame(cell.location.y,object.location.y):
        if cell.location.x>object.location.x:#6
            input=moveLeft(cell)
        if cell.location.x<object.location.x:#2
            input=moveRight(cell)
    elif cell.location.y>object.location.y:#target is above cell
        if kindOfTheSame(cell.location.x,object.location.x):#0
            input=moveUp(cell)
        elif cell.location.x>object.location.x:#7
            input=moveUL(cell)
        elif cell.location.x<object.location.x:#1
            input=moveUR(cell)
    elif cell.location.y<object.location.y:#target is under cell
        if kindOfTheSame(cell.location.x,object.location.x):#4
            input=moveDown(cell)
        elif cell.location.x>object.location.x:#5
            input=moveDL(cell)
        elif cell.location.x<object.location.x:#3
            input=moveDR(cell)
    return input
#DONE
def kindOfTheSame(a1,a2):
    if a1==a2 or a1+1==a2 or a1-1==a2 or a1+2==a2 or a1-2==a2 or a1+3==a2 or a1-3==a2 or a1-4==a2 or a1+4==a2 or a1+5==a2 or a1-5==a2 or a1-6==a2 or a1+6==a2:
        return True
    else:
        return False
def moveUR(cell):
    input=[]
    if cell.angle==1:#1
        input.append("Up")
    elif 1<cell.angle<=5:#2345
        input.append("OLeft")
    elif 6<=cell.angle<=7 or 0==cell.angle:#670
        input.append("ORight")
    return input
def moveDR(cell):
    input=[]
    if cell.angle==3:#3
        input.append("Up")
    elif 3<cell.angle<=7:#4567
        input.append("OLeft")
    elif 0<=cell.angle<=2 :#012
        input.append("ORight")
    return input
def moveDL(cell):
    input=[]
    if cell.angle==5:#5
        input.append("Up")
    elif 1<=cell.angle<5:#1234
        input.append("ORight")
    elif 6<=cell.angle<=7 or 0==cell.angle:#670
        input.append("OLeft")
    return input
def moveUL(cell):
    input=[]
    if cell.angle==7:#7
        input.append("Up")
    elif 3<=cell.angle<7:#3456
        input.append("ORight")
    elif 0<=cell.angle<=2 :#012
        input.append("OLeft")
    return input
def moveRight(cell):
    input=[]
    if cell.angle==2:#2
        input.append("Up")
    if 2<cell.angle<=6:#3456
        input.append("OLeft")
    if cell.angle==7 or 0<=cell.angle<2:#701
        input.append("ORight")
    return input
def moveLeft(cell):
    input=[]
    if cell.angle==6:#6
        input.append("Up")
    if 2<cell.angle<6:#345
        input.append("ORight")
    if 6<cell.angle<8 or 0<=cell.angle<=2:#7012
        input.append("OLeft")
    return input
def moveUp(cell):
    input=[]
    if cell.angle==0:#0
        input.append("Up")
    if cell.angle>4:#567
        input.append("ORight")
    if 4>=cell.angle>0:#1234
        input.append("OLeft")
    return input
def moveDown(cell):
    input=[]
    if cell.angle==4:#4
        input.append("Up")
    if cell.angle<4:#0123
        input.append("ORight")
    if cell.angle>4:#567
        input.append("OLeft")
    return input
#DONE
def closestFood(cell,foodList):
    big=10000000
    index=None
    for food in foodList:
        if math.sqrt(((cell.location.x-food.location.x)**2)+((cell.location.y-food.location.y)**2))<big:
            big=math.sqrt(((cell.location.x-food.location.x)**2)+((cell.location.y-food.location.y)**2))
            index=food
    return index
#DONE
def closestMate(cell,cellList):
    big=10000000
    index=None
    for Cell in cellList:
        if math.sqrt(((cell.location.x-Cell.location.x)**2)+((cell.location.y-Cell.location.y)**2))<big:
            big=math.sqrt(((cell.location.x-Cell.location.x)**2)+((cell.location.y-Cell.location.y)**2))
            index=Cell
    return index
#DONE
def bestMate(cell,cellList):
    diff=-1000000
    end=None
    for curr1 in cellList:
        for curr2 in cellList:
            if math.fabs(compareCells(curr1,curr2))>diff:
                if compareCells(curr1,curr2)>0 and curr1.mode=="m":
                    end=curr1
                    diff=math.fabs(compareCells(curr1,curr2))
                elif compareCells(curr1,curr2)<0 and curr2.mode=="m":
                    end=curr2
                    diff=math.fabs(compareCells(curr1,curr2))
                else:
                    i=random.randint(0,1)
                    if i==0 and curr1.mode=="m":
                        end=curr1
                        diff=math.fabs(compareCells(curr1,curr2))
                    elif curr2.mode=="m":
                        end=curr2
                        diff=math.fabs(compareCells(curr1,curr2))
    return end
#DONE
def compareCells(c1,c2):
    p1=0
    p2=0
    #lifeTime 11p
    if c1.lifeTime >c2.lifeTime:
        p1+=11
    if c1.lifeTime <c2.lifeTime:
        p2+=11
    #AI 10p
    if c1.AI >c2.AI:
        p1+=10
    if c1.AI <c2.AI:
        p2+=10
    #carnivore 9p
    if c1.carnivore >c2.carnivore:
        p1+=9
    if c1.carnivore <c2.carnivore:
        p2+=9
    #speed 8p
    if c1.speed >c2.speed:
        p1+=8
    if c1.speed <c2.speed:
        p2+=8
    #timeToLay 7p
    if c1.timeToLay >c2.timeToLay:
        p1+=7
    if c1.timeToLay <c2.timeToLay:
        p2+=7
    #strength 6p
    if c1.strength  >c2.strength :
        p1+=6
    if c1.strength  <c2.strength :
        p2+=6
    #vision 5p
    if c1.vision >c2.vision:
        p1+=5
    if c1.vision <c2.vision:
        p2+=5
    #lifeWithdraw 4p
    if c1.lifewithdraw >c2.lifewithdraw:
        p1+=4
    if c1.lifewithdraw <c2.lifewithdraw:
        p2+=4
    #foodWithdraw 3p
    if c1.foodWithdraw >c2.foodWithdraw:
        p1+=3
    if c1.foodWithdraw <c2.foodWithdraw:
        p2+=3
    #eggWithdraw 2p
    if c1.eggwithdraw >c2.eggwithdraw:
        p1+=2
    if c1.eggwithdraw <c2.eggwithdraw:
        p2+=2
    #eggHatchTime 1p
    if c1.eggHatchTime >c2.eggHatchTime:
        p1+=1
    if c1.eggHatchTime <c2.eggHatchTime:
        p2+=1
    return p1-p2
#DONE
def validMate(cell):
    if cell==None:
        return False
    if isinstance(cell,classes.baseCell):
        if cell.mode=="m" and insideCircle(cell):
            return True
    return False