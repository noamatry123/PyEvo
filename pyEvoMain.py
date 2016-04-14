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

    running = True
    #hi
    text="Empty"
    pygame.init()

    ##load
    choice=easygui.boolbox("Choose option?","",["Load Last Game","New Game"]) ##new/load
    if choice==0:##new
        consts.loadedGame=False
    else:##load
        consts.loadedGame=True

    ##choose movement
    choice=easygui.boolbox("Choose option?","",["Keyboard","Mouse"]) ##new/load
    if choice==0:##Mouse
        consts.mouse_control=True
    else:##Keyboard
        consts.mouse_control=False

    ##godmode: delete later
    choice=easygui.boolbox("Godmode?","",["No","Yes"])
    if choice==0:
        consts.godmode=True

    choice=easygui.boolbox("Fulscreen?","",["Yes","No"])
    if choice==0:
        screen = pygame.display.set_mode((consts.screenwidth, consts.screenheight))
    else:
        screen = pygame.display.set_mode((consts.screenwidth, consts.screenheight),pygame.FULLSCREEN)



    algoModule = algorithm.pyAlgorithm(consts.screenwidth,consts.screenheight)
    graphics.screen=screen
    graphics.clock = pygame.time.Clock()
    while running:
        algoModule.nextStep(text)
        running,text = graphics.drawBoard(algoModule.myCell, algoModule.cellList, algoModule.foodList,[algoModule.myEggs, algoModule.cellEggs])


if __name__ == "__main__":
    main()
