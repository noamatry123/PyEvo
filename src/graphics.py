__author__ = 'user-pc'
import pygame
import time
class pyGraphics:
    __framerate=60
    __screenwidth=800
    __screenheight=600
    __screen=None
    __clock=None
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((self.__screenwidth, self.__screenheight))
        self.__clock = pygame.time.Clock()
        self.__running=True
    def drawBoard(self,playerCell,cellList,foodList,eggList):
        self.__screen.fill((255,0,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        pygame.draw.circle(self.__screen,(0,0,0),(playerCell.location.getTupple()),10)
        self.__clock.tick(self.__framerate)
        pygame.display.flip()
        return True