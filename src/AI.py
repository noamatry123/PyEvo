__author__ = 'user-pc'
import pygame
import graphics
import classes
import random
import math

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
    foodsee,cellsee=look4Food(currCell,foodList,cellList)
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

def look4Food(cell,foodList,cellList):
    foodsee=[]
    cellsee=[]
    for food in foodList:
        if math.sqrt(((cell.location.x-food.location.x)**2)+((cell.location.y-food.location.y)**2))<cell.vision:
            foodsee.append(food)
    for curr in cellList:
        if math.sqrt(((cell.location.x-curr.location.x)**2)+((cell.location.y-curr.location.y)**2))<cell.vision:
            cellsee.append(curr)
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
"""
ai2=random food,random mate
"""
def AI2(cell,foodList,cellList):
    input=[]
    if len(foodList)==0:
        input=AI1(cell)
        return input
    ##search mate if its mating time
    if cell.timeToLayLeft<cell.timeToLay/3 and len(cellList)!=0:
        i=random.randint(0,len(cellList)-1)
        if cell!=cellList[i]:
            if cell.target==None:
                cell.target=cellList[i]
            else:
                if (cell.target in foodList) or (cell.target in cellList):
                    pass
                else:
                    cell.target=cellList[i]
            input=goto(cell,cell.target)
            if cell.mode!="m":
                input.append("c")
            if cell.timeToLayLeft==0 and cell.lastMother!=cell:##lay egg if possible
                input.append("a")
            return input
    ##search food
    a=0
    if cell.carnivore==1:
        a=random.randint(0,1)
        if a==1:#vegan food
            i=random.randint(0,len(foodList)-1)
            if cell.target==None:
                cell.target=foodList[i]
            else:
                if (cell.target in foodList) or (cell.target in cellList):
                    pass
                else:
                    cell.target=foodList[i]
            input=goto(cell,cell.target)
        else:#real food
            i=random.randint(0,len(cellList)-1)
            if cell.target==None:
                cell.target=cellList[i]
            else:
                if (cell.target in foodList) or (cell.target in cellList):
                    pass
                else:
                    cell.target=cellList[i]
            input=goto(cell,cell.target)
            if cell.mode!="c":
                input.append("c")
    else:
        i=random.randint(0,len(foodList)-1)
        if cell.target==None:
            cell.target=foodList[i]
        else:
            if (cell.target in foodList) or (cell.target in cellList):
                pass
            else:
                cell.target=foodList[i]
        input=goto(cell,cell.target)
    if cell.timeToLayLeft==0 and cell.lastMother!=cell:##lay egg if possible
            input.append("a")
    return input
"""
ai3=closest food,closest mate
"""
def AI3(cell,foodList,cellList):
    input=[]
    if len(foodList)==0:
        input=AI1(cell)
        return input
    if cell.timeToLayLeft<cell.timeToLay/3:
        target=closestFood(cell,cellList)
        if cell!=target:
            if cell.target==None:
                cell.target=target
            else:
                if (cell.target in foodList) or (cell.target in cellList):
                    pass
                else:
                    cell.target=target
            input=goto(cell,cell.target)
            if cell.mode!="m":
                input.append("c")
            if cell.timeToLayLeft==0 and cell.lastMother!=cell:##lay egg if possible
                input.append("a")
            return input
    ##search food
    a=0
    if cell.carnivore==1:
        a=random.randint(0,1)
        if a==1:#vegan food
            if cell.target==None:
                cell.target=closestFood(cell,foodList)
            else:
                if (cell.target in foodList) or (cell.target in cellList):
                    pass
                else:
                    cell.target=closestFood(cell,foodList)
            input=goto(cell,cell.target)
        else:#real food
            if cell.target==None:
                cell.target=closestFood(cell,cellList)
            else:
                if (cell.target in foodList) or (cell.target in cellList):
                    pass
                else:
                    cell.target=closestFood(cell,cellList)
            input=goto(cell,cell.target)
            if cell.mode!="c":
                input.append("c")
    else:
        if cell.target==None:
            cell.target=closestFood(cell,foodList)
        else:
            if (cell.target in foodList) or (cell.target in cellList):
                pass
            else:
                cell.target=closestFood(cell,foodList)
        input=goto(cell,cell.target)
    if cell.timeToLayLeft==0 and cell.lastMother!=cell:##lay egg if possible
            input.append("a")
    return input
"""
ai4-closest food,best mate,does move across
"""
def AI4(cell,foodList,cellList):
    input=[]
    if len(foodList)==0:
        input=AI1(cell)
        return input
    if cell.timeToLayLeft<cell.timeToLay/3:
        #target=bestMate(cell,cellList)##fill
        target=closestFood(cell,cellList)
        if cell!=target:
            if cell.target==None:
                cell.target=target
            else:
                if (cell.target in foodList) or (cell.target in cellList):
                    pass
                else:
                    cell.target=target
            input=goodGoTo(cell,cell.target)
            if cell.mode!="m":
                input.append("c")
            if cell.timeToLayLeft==0 and cell.lastMother!=cell:##lay egg if possible
                input.append("a")
            return input
    ##search food
    a=0
    if cell.carnivore==1:
        a=random.randint(0,1)
        if a==1:#vegan food
            if cell.target==None:
                cell.target=closestFood(cell,foodList)
            else:
                if (cell.target in foodList) or (cell.target in cellList):
                    pass
                else:
                    cell.target=closestFood(cell,foodList)
            input=goodGoTo(cell,cell.target)
        else:#real food
            if cell.target==None:
                cell.target=closestFood(cell,cellList)
            else:
                if (cell.target in foodList) or (cell.target in cellList):
                    pass
                else:
                    cell.target=closestFood(cell,cellList)
            input=goodGoTo(cell,cell.target)
            if cell.mode!="c":
                input.append("c")
    else:
        if cell.target==None:
            cell.target=closestFood(cell,foodList)
        else:
            if (cell.target in foodList) or (cell.target in cellList):
                pass
            else:
                cell.target=closestFood(cell,foodList)
        input=goodGoTo(cell,cell.target)
    if cell.timeToLayLeft==0 and cell.lastMother!=cell:##lay egg if possible
            input.append("a")
    return input
def bestMate(cell,cellList):
    pass
def goto(cell,object):
    input=[]
    if kindOfTheSame(cell.location.y,object.location.y):
        if cell.location.x>object.location.x:#6
            input=moveLeft(cell)
        if cell.location.x<object.location.x:#2
            input=moveRight(cell)
    if cell.location.y<object.location.y:#target is under cell
        if kindOfTheSame(cell.location.x,object.location.x):#4
            input=moveDown(cell)
        if cell.location.x>object.location.x:#5
            if cell.location.y!=object.location.y:#check if same y if not move down
                input=moveDown(cell)
            else:#if yes move left
                input=moveLeft(cell)
        if cell.location.x<object.location.x:#3
            if cell.location.y!=object.location.y:#check if same y if not move down
                input=moveDown(cell)
            else:#if yes move right
                input=moveRight(cell)
    if cell.location.y>object.location.y:#target is above cell
        if kindOfTheSame(cell.location.x,object.location.x):#0
            input=moveUp(cell)
        if cell.location.x>object.location.x:#7
            if cell.location.y!=object.location.y:#check if same y if not move Up
                input=moveUp(cell)
            else:#if yes move right
                input=moveLeft(cell)
        if cell.location.x<object.location.x:#1
            if cell.location.y!=object.location.y:#check if same y if not move Up
                input=moveUp(cell)
            else:#if yes move left
                input=moveRight(cell)
    return input
def goodGoTo(cell,object):
    input=[]
    input=AI1(cell)
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
def kindOfTheSame(a1,a2):
    if a1==a2 or a1+1==a2 or a1-1==a2 or a1+2==a2 or a1-2==a2 or a1+3==a2 or a1-3==a2 or a1-4==a2 or a1+4==a2:
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
def closestFood(cell,foodList):
    big=10000000
    index=None
    for food in foodList:
        if math.sqrt(((cell.location.x-food.location.x)**2)+((cell.location.y-food.location.y)**2))<big:
            big=math.sqrt(((cell.location.x-food.location.x)**2)+((cell.location.y-food.location.y)**2))
            index=food
    return index