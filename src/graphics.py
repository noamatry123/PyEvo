__author__ = 'user-pc'
import pygame
import time
import classes
screenwidth=800
screenheight=600
class pyGraphics:

    __framerate=0
    __screenwidth=0
    __screenheight=0
    __screen=None
    __clock=None
    __myfont =None
    def __init__(self,framerate,width,height):
        self.__framerate=framerate
        self.__screenheight=height
        self.__screenwidth=width
        pygame.init()
        self.__myfont= pygame.font.SysFont("Ariel", 20)
        self.__screen = pygame.display.set_mode((self.__screenwidth, self.__screenheight))
        self.__clock = pygame.time.Clock()
        self.__running=True
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
        return True