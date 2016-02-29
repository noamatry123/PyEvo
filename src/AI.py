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
    i=random.randint(len(foodList))

def AI3(cell,foodList,cellList):
    pass
def AI4(cell,foodList,cellList):
    pass
def goto(cell,object):
    input=[]
    if cell.location.y<object.location.y:
        if cell.location.x==object.location.x:#1
            if cell.angle==4:
                input.append("Up")
        if cell.location.x>object.location.x:#2
            pass
        if cell.location.x<object.location.x:#3
            pass
    if cell.location.y>object.location.y:
        if cell.location.x==object.location.x:#4
            pass
        if cell.location.x>object.location.x:#5
            pass
        if cell.location.x<object.location.x:#6
            pass
    if cell.location.y==object.location.y:
        if cell.location.x>object.location.x:#7
            pass
        if cell.location.x<object.location.x:#8
            pass