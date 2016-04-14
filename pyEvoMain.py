__author__ = 'user-pc'
import classes
import graphics
import algorithm
import easygui

import consts
import pygame
def main():
    values=easygui.multenterbox("Display settings: ","",["Width","Height","Fullscreen"],["800","600","no"])
    consts.screenwidth=int(values[0])
    consts.screenheight=int(values[1])
    if values[2]!="Yes":
        screen = pygame.display.set_mode((consts.screenwidth, consts.screenheight))
    else:
        screen = pygame.display.set_mode((consts.screenwidth, consts.screenheight),pygame.FULLSCREEN)
    running = True
    #hi
    text="Empty"
    pygame.init()

    graphics.screen=screen
    graphics.clock = pygame.time.Clock()
    graphics.askBoard("menu")
    algoModule = algorithm.pyAlgorithm(consts.screenwidth,consts.screenheight)

    while running:
        algoModule.nextStep(text)
        running,text = graphics.drawBoard(algoModule.myCell, algoModule.cellList, algoModule.foodList,[algoModule.myEggs, algoModule.cellEggs])


if __name__ == "__main__":
    main()
