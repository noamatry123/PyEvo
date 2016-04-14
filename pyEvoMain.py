__author__ = 'user-pc'
import classes
import graphics
import algorithm
import easygui

import consts
import pygame
def main():
    consts.screenwidth=int(easygui.enterbox("Enter width","","1440"))
    consts.screenheight=int(easygui.enterbox("Enter height","","900"))
    choice=easygui.boolbox("Fulscreen?","",["Yes","No"])
    if choice==0:
        screen = pygame.display.set_mode((consts.screenwidth, consts.screenheight))
    else:
        screen = pygame.display.set_mode((consts.screenwidth, consts.screenheight),pygame.FULLSCREEN)
    running = True
    #hi
    text="Empty"
    pygame.init()

    algoModule = algorithm.pyAlgorithm(consts.screenwidth,consts.screenheight)
    graphics.screen=screen
    graphics.clock = pygame.time.Clock()
    graphics.askBoard("menu")
    while running:
        algoModule.nextStep(text)
        running,text = graphics.drawBoard(algoModule.myCell, algoModule.cellList, algoModule.foodList,[algoModule.myEggs, algoModule.cellEggs])


if __name__ == "__main__":
    main()
