__author__ = 'user-pc'
import pygame
import time
class pyGraphics:
    __framerate=120
    __screenwidth=800
    __screenheight=600

    __cellList=[]
    __foodList=[]
    __eggList=[]
    __screen=None
    __clock=None
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((self.__screenwidth, self.__screenheight))
        self.__clock = pygame.time.Clock()
        self.__running=True
    def drawBoard(self):
        self.__screen.fill((255,0,255))