__author__ = 'user-pc'
import sys, os
#sys.path.append(os.getcwd())
import graphics
import algorithm
import easygui

import consts
import pygame
def main():
    values=easygui.multenterbox("Display settings: ","",["Width","Height","Fullscreen","Sandbox","Tutorial"],["1366","766","Yes","No","No"])
    consts.screenwidth=int(values[0])
    consts.screenheight=int(values[1])
    consts.Center.location=consts.Location1(consts.screenwidth,consts.screenheight)
    if values[3]!="No":
        consts.sandbox=True
    if values[4]!="No":
        if(easygui.msgbox("Tutorial starting", ok_button="Press 'p' to continiue with the tutorial")):
            pass
        consts.tutorial=True
    if values[2]!="Yes":
        screen = pygame.display.set_mode((consts.screenwidth, consts.screenheight))
    else:
        screen = pygame.display.set_mode((consts.screenwidth, consts.screenheight),pygame.FULLSCREEN)
        consts.fs=True
    running = True
    #hi
    text="Empty"
    pygame.init()

    graphics.screen=screen
    graphics.clock = pygame.time.Clock()
    if consts.tutorial:
        graphics.tut()
    if not consts.sandbox:
        graphics.askBoard("menu")
        algoModule = algorithm.pyAlgorithm(consts.screenwidth,consts.screenheight,consts.lvl)
    else:
        graphics.sandbox()

    while running:
        algoModule.nextStep(text)
        running,text = graphics.drawBoard(algoModule.myCell, algoModule.cellList, algoModule.foodList,[algoModule.myEggs, algoModule.cellEggs])

if __name__ == "__main__":
    main()
