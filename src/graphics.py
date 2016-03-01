__author__ = 'user-pc'
import pygame
import time
import classes
import easygui
import math
import subprocess
import sys

screenwidth=800
screenheight=600
class pyGraphics:

    __framerate=0
    __screenwidth=0
    __screenheight=0
    __screen=None
    __clock=None
    __myfont =None
    last_clickcheck=None
    def __init__(self,framerate,width,height):
        self.__framerate=framerate
        self.__screenheight=height
        self.__screenwidth=width
        pygame.init()
        self.__myfont= pygame.font.SysFont("Ariel", 20)
        self.__screen = pygame.display.set_mode((self.__screenwidth, self.__screenheight))
        self.__clock = pygame.time.Clock()
        self.__running=True
        self.last_clickcheck=0
    def printAtt(self,playerCell):
        counter=0
        for att in playerCell.getAtts():
            label = self.__myfont.render(att,1, (255,255,0))
            self.__screen.blit(label, (0,counter))
            counter+=20
    def drawBoard(self,playerCell,cellList,foodList,eggList):
        IDtempfont=pygame.font.SysFont("Ariel", 20)
        ##fill screen
        self.__screen.fill((255,0,255))
        ##handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        ##hadndle drawing cells and food
        for cell in cellList:
            pygame.draw.circle(self.__screen,(255,0,0),(cell.location.getTupple()),cell.rad)
            pygame.draw.circle(self.__screen,(10,255,10),(cell.location_compensated()),2)
            ##draw IDs:
            label = IDtempfont.render(str(cell.ID), 1, (255,255,0))
            self.__screen.blit(label,(cell.location.x,cell.location.y))
        for food in foodList:
            pygame.draw.circle(self.__screen,(80,255,80),(food.location.getTupple()),food.rad)
        ##prints attributes
        self.printAtt(playerCell)
        ##draw player eggs
        for egg in eggList[0]:
            pygame.draw.circle(self.__screen,(255,255,255),(egg.location.getTupple()),egg.rad)
        for egg in eggList[1]:
            pygame.draw.circle(self.__screen,(255,255,255),(egg.location.getTupple()),egg.rad)
        ##draw player
        pygame.draw.circle(self.__screen,(0,0,0),(playerCell.location.getTupple()),playerCell.rad)
        pygame.draw.circle(self.__screen,(10,255,10),(playerCell.location_compensated()),2)
        ##draw player ID
        label = IDtempfont.render(str(playerCell.ID), 1, (255,255,0))
        self.__screen.blit(label,(playerCell.location.x,playerCell.location.y))
        if playerCell.dead:
            pygame.draw.rect(self.__screen,(0,0,0),(0,0,800,600))
        ##tick and flip
        self.__clock.tick(self.__framerate)
        pygame.display.flip()

        self.checkClickAndPrintToScreen(cellList)
        return True
    def checkClickAndPrintToScreen(self,cellList):
        if pygame.mouse.get_pressed()[0]==True:
            pos = pygame.mouse.get_pos()
            for cell in cellList:
                if math.sqrt(((pos[0]-cell.location.x)**2)+((pos[1]-cell.location.y)**2))<cell.rad:
                    if pygame.time.get_ticks()>self.last_clickcheck+500: ##500ms since last successful click
                        self.last_clickcheck=pygame.time.get_ticks()
                        text=""
                        for i in xrange(0,len(cell.getAtts())):
                            text+=cell.getAtts()[i]+"\n"
                        cmd='cscript src/MessageBox.vbs "This will be shown in a popup."'
                        proc = subprocess.Popen([cmd], shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)