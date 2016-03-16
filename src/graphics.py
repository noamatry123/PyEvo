__author__ = 'user-pc'
import pygame
import time
import classes
import math
import termcolor
import easygui
import consts
import Buttons

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
        self.__myfont1= pygame.font.SysFont("Ariel", 40)
        choice=easygui.boolbox("Fulscreen?","",["Yes","No"])
        if choice==0:
            self.__screen = pygame.display.set_mode((self.__screenwidth, self.__screenheight))
        else:
            self.__screen = pygame.display.set_mode((self.__screenwidth, self.__screenheight),pygame.FULLSCREEN)
        self.__clock = pygame.time.Clock()
        self.__running=True
        self.last_clickcheck=0

    def printAtt(self,playerCell):
        counter=0
        for att in playerCell.getUsefullAtts():
            label = self.__myfont.render(att,1, (255,255,0))
            self.__screen.blit(label, (0,counter))
            counter+=20
    def askBoard(self,mode, text):
        self.Button1 = Buttons.Button()
        self.__screen.fill((255,0,255))

        screencenter=(self.__screenwidth/2-100,self.__screenheight/2-100)
        screencenter_below=(self.__screenwidth/2-100,(self.__screenheight/2+(self.__screenheight/4)))
        ##switch mode
        if mode=="Prompt":
            label = self.__myfont1.render(text, 1, (0,0,0))
            self.__screen.blit(label,screencenter)
            #Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
            self.Button1.create_button(self.__screen, (107,142,35), screencenter_below[0], screencenter_below[1], 200,    100,    0,        "Okay", (255,255,255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False, "End"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.Button1.pressed(pygame.mouse.get_pos()):
                        print "Give me a command!"
                        return True, "Okay"

        self.__clock.tick(self.__framerate)
        pygame.display.flip()
        return True,"Empty"

    def drawBoard(self,playerCell,cellList,foodList,eggList):
        if consts.askingQuestion: ##there is a pending question / prompt
            return self.askBoard("Prompt","Continue?")
        IDtempfont=pygame.font.SysFont("Ariel", 20)
        ##fill screen
        self.__screen.fill((255,0,255))
        ##handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False,"End"
        ##hadndle drawing cells and food
        for cell in cellList:
            if cell.timeToHurt%2==0:
                pygame.draw.circle(self.__screen,(255,0,0),(cell.location.getTupple()),cell.rad)
                pygame.draw.circle(self.__screen,(10,255,10),(cell.location_compensated()),2)
                ##draw IDs:
                label = IDtempfont.render(str(cell.ID), 1, (255,255,0))
                self.__screen.blit(label,(cell.location.x+5,cell.location.y))
                ##draw life:
                label = IDtempfont.render(str(cell.lifeTimeLeft), 1, (0,0,0))
                self.__screen.blit(label,(cell.location.x-15,cell.location.y))
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
        ##pygame.draw.circle(self.__screen,(0,0,0),(playerCell.location.getTupple()),playerCell.rad)
        ##pygame.draw.circle(self.__screen,(10,255,10),(playerCell.location_compensated()),2)
        self.__screen.blit(playerCell.image,(playerCell.location.x-playerCell.rad,playerCell.location.y-playerCell.rad))

        ##draw player ID
        label = IDtempfont.render(str(playerCell.ID), 1, (255,255,0))
        self.__screen.blit(label,(playerCell.location.x,playerCell.location.y))


        if playerCell.dead:
            pygame.draw.rect(self.__screen,(0,0,0),(0,0,consts.screenwidth,consts.screenheight))
        ##tick and flip


        self.__clock.tick(self.__framerate)
        pygame.display.flip()

        self.checkClickAndPrintToScreen(cellList)
        return True,"Empty"
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
                        termcolor.cprint(text,"green")