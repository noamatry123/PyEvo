__author__ = 'user-pc'
import pygame
import graphics
import classes
import random
import math

"""
ai0=random and not moving while rotating
ai1=random movement
ai2=random food,random mate
ai3=closest food,closest mate
ai4-closest food,best mate

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
    elif currCell.AI==4:
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
    i=random.randint(0,50)
    if i==0:
        input.append("ORight")
    if i==1:
        input.append("OLeft")
    input.append("Up")
    return input
def AI2(cell,foodList,cellList):
    input=[]
    if 0==1:
        pass
    if len(foodList)==0:
        input=AI1(cell)
        return input
    i=random.randint(0,len(foodList)-1)
    if cell.target==None:
        cell.target=foodList[i]
    else:
        if (cell.target in foodList) or (cell.target in cellList):
            pass
        else:
            cell.target=foodList[i]
    input=goto(cell,cell.target)
    return input
def AI3(cell,foodList,cellList):
    input=[]
    if len(foodList)==0:
        input=AI1(cell)
        return input
    cell.target=closestFood(cell,foodList)
    if cell.target==None:
        cell.target=closestFood(cell,foodList)
    else:
        if (cell.target in foodList) or (cell.target in cellList):
            pass
        else:
            cell.target=closestFood(cell,foodList)
    input=goto(cell,cell.target)
    return input
def AI4(cell,foodList,cellList):
    pass
def goto(cell,object):
    input=[]
    if cell.location.y<object.location.y:
        if cell.location.x==object.location.x or cell.location.x+2==object.location.x or cell.location.x-2==object.location.x or cell.location.x+2==object.location.x or cell.location.x-2==object.location.x:#1
            input=moveDown(cell)
        if cell.location.x>object.location.x:#2
            if cell.location.y!=object.location.y:#check if same y if not move down
                input=moveDown(cell)
            else:#if yes move left
                input=moveLeft(cell)
        if cell.location.x<object.location.x:#3
            if cell.location.y!=object.location.y:#check if same y if not move down
                input=moveDown(cell)
            else:#if yes move right
                input=moveRight(cell)
    if cell.location.y>object.location.y:
        if cell.location.x==object.location.x or cell.location.x+2==object.location.x or cell.location.x-2==object.location.x or cell.location.x+2==object.location.x or cell.location.x-2==object.location.x:#4
            input=moveUp(cell)
        if cell.location.x>object.location.x:#5
            if cell.location.y!=object.location.y:#check if same y if not move Up
                input=moveUp(cell)
            else:#if yes move right
                input=moveRight(cell)
        if cell.location.x<object.location.x:#6
            if cell.location.y!=object.location.y:#check if same y if not move Up
                input=moveUp(cell)
            else:#if yes move left
                input=moveLeft(cell)
    if cell.location.y==object.location.y or cell.location.y+3==object.location.y or cell.location.y-3==object.location.y or cell.location.y+2==object.location.y or cell.location.y-2==object.location.y:
        if cell.location.x>object.location.x:#7
            input=moveLeft(cell)
        if cell.location.x<object.location.x:#8
            input=moveRight(cell)
    return input
def moveRight(cell):
    input=[]
    if cell.angle==2:
        input.append("Up")
    if 2<cell.angle<=6:
        input.append("OLeft")
    if cell.angle==7 or 0<=cell.angle<2:
        input.append("ORight")
    return input
def moveLeft(cell):
    input=[]
    if cell.angle==6:
        input.append("Up")
    if 2<cell.angle<6:
        input.append("ORight")
    if 6<cell.angle<8 or 0<=cell.angle<=2:
        input.append("OLeft")
    return input
def moveUp(cell):
    input=[]
    if cell.angle==0:
        input.append("Up")
    if cell.angle>4:
        input.append("ORight")
    if 4>=cell.angle>0:
        input.append("OLeft")
    return input
def moveDown(cell):
    input=[]
    if cell.angle==4:
        input.append("Up")
    if cell.angle<4:
        input.append("ORight")
    if cell.angle>4:
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