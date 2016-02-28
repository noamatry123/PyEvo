__author__ = 'user-pc'
import pygame
import graphics
import classes
import random
import math

"""
ai0=random movement
ai1=random food,random mate
ai2=closest food,closest mate
ai3-closest food,best mate

"""
class AI:
    def nextStep(self,playerCell,cellList,foodList,currCell):
        foodsee=[]
        cellsee=[]
        foodsee,cellsee=self.look4Food(currCell,foodList,cellList)
        if currCell.AI==0:
            self.AI0(currCell)
        elif currCell.AI==1:
            self.AI1(currCell,foodsee,cellsee)
        elif currCell.AI==2:
            self.AI2(currCell,foodsee,cellsee)
        elif currCell.AI==3:
            self.AI3(currCell,foodsee,cellsee)

    def look4Food(self,cell,foodList,cellList):
        foodsee=[]
        cellsee=[]
        for food in foodList:
            if math.sqrt(((cell.location.x-food.location.x)**2)+((cell.location.y-food.location.y)**2))<cell.vision:
                foodsee.append(food)
        for curr in cellList:
            if math.sqrt(((cell.location.x-curr.location.x)**2)+((cell.location.y-curr.location.y)**2))<cell.vision:
                cellsee.append(curr)
        return foodsee,cellsee
    def AI0(self,cell):
        pass
        pass
    def AI1(self,cell,foodList,cellList):
        pass
    def AI2(self,cell,foodList,cellList):
        pass
    def AI3(self,cell,foodList,cellList):
        pass
    def action(self,cell,inputlist):
        for item in inputlist:
            if item=="Left":
                cell.changeAngle(-1)
            if item=="Right":
                cell.changeAngle(1)
        if "Up" in inputlist:
            cell.move()
        ##handle food and life
        self.checkEat(cell)
        cell.consumeFood(self._counter)
        cell.consumeLife(self._counter)
        cell.consumeEggTime(self._counter)
        cell.checkRIP()
        for cell in self.cellList:
            self.checkEat(cell)
            cell.consumeFood(self._counter)
            cell.consumeLife(self._counter)
            cell.checkRIP()
            if cell.dead:
                self.cellList.remove(cell)
        if "a" in inputlist:
            if cell.timeToLayLeft==0:
                self.myEggs.append(cell.layEgg())
        self.__kinput=[]