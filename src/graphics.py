__author__ = 'user-pc'
import pygame
import time
import classes
import math
import termcolor
import easygui
import consts
import Buttons
screen=None
clock=None
myfont =pygame.font.SysFont("Ariel", 20)
myfont1=pygame.font.SysFont("Ariel", 30)
last_clickcheck=None

def printAtt(playerCell):
    counter=0
    for att in playerCell.getUsefullAtts():
        label = myfont.render(att,1, (255,255,0))
        screen.blit(label, (0,counter))
        counter+=20
def askBoard(mode, text,option1="",option2=""):
    Button1 = Buttons.Button()
    Button2 = Buttons.Button()
    screen.fill((255,0,255))

    screencenter=(consts.screenwidth/2,consts.screenheight/2)
    screencenter_below=(consts.screenwidth/2-100,(consts.screenheight/2+(consts.screenheight/4)))
    ##switch mode
    if mode=="Prompt":
        ptext=text.split("\n")
        plabel=[]
        for p in ptext:
            plabel.append(myfont1.render(p, 1, (0,0,0)))
        for i in range(0,len(plabel)):
            screen.blit(plabel[i],(screencenter[0]-100,10+i*35))
        #Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
        Button1.create_button(screen, (107,142,35), screencenter_below[0], screencenter_below[1], 200,    100,    0,        "Okay", (255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Button1.pressed(pygame.mouse.get_pos()):
                    return "Okay"
    if mode=="manual":
        ptext=text.split("\n")
        plabel=[]
        for p in ptext:
            plabel.append(myfont1.render(p, 1, (0,0,0)))
        for i in range(0,len(plabel)):
            screen.blit(plabel[i],(screencenter[0]-100,10+i*20))
        #Parameters:          surface,      color,       x,                         y,              length, height, width,       text,      text_color
        Button1.create_button(screen, (107,142,35), 40,                        consts.screenheight-40-100, 300,    100,    0,        option1, (255,255,255))
        Button2.create_button(screen, (107,142,35), consts.screenwidth-40-300, consts.screenheight-40-100, 300,    100,    0,        option2, (255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Button1.pressed(pygame.mouse.get_pos()):
                    return option1
                if Button2.pressed(pygame.mouse.get_pos()):
                    return option2
    clock.tick(consts.framerate)
    pygame.display.flip()
    return "Empty"

def drawBoard(playerCell,cellList,foodList,eggList):
    IDtempfont=pygame.font.SysFont("Ariel", 20)
    ##fill screen
    screen.fill((255,0,255))
    ##handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False,"End"
    ##hadndle drawing cells and food
    for cell in cellList:
        if cell.timeToHurt%2==0:
            ##pygame.draw.circle(screen,(255,0,0),(cell.location.getTupple()),cell.rad)
            ##pygame.draw.circle(screen,(10,255,10),(cell.location_compensated()),2)
            screen.blit(cell.image,(cell.location.x-cell.rad,cell.location.y-cell.rad))

            ##draw IDs:
            label = IDtempfont.render(str(cell.ID), 1, (255,255,0))
            screen.blit(label,(cell.location.x+5,cell.location.y))
            ##draw life:
            label = IDtempfont.render(str(cell.lifeTimeLeft), 1, (0,0,0))
            screen.blit(label,(cell.location.x-15,cell.location.y))
    for food in foodList:
        pygame.draw.circle(screen,(80,255,80),(food.location.getTupple()),food.rad)
    ##prints attributes
    printAtt(playerCell)
    ##draw player eggs
    for egg in eggList[0]:
        pygame.draw.circle(screen,(10,10,255),(egg.location.getTupple()),egg.rad)
    for egg in eggList[1]:
        pygame.draw.circle(screen,(10,10,255),(egg.location.getTupple()),egg.rad)
    ##draw player
    ##pygame.draw.circle(screen,(0,0,0),(playerCell.location.getTupple()),playerCell.rad)
    ##pygame.draw.circle(screen,(10,255,10),(playerCell.location_compensated()),2)
    screen.blit(playerCell.image,(playerCell.location.x-playerCell.rad,playerCell.location.y-playerCell.rad))

    ##draw player ID
    label = IDtempfont.render(str(playerCell.ID), 1, (255,255,0))
    screen.blit(label,(playerCell.location.x,playerCell.location.y))


    if playerCell.dead:
        choice = None
        while choice!="Okay":
            choice=askBoard("Prompt","You died!\nYou lived " + str(consts.counter/consts.framerate) + " Seconds!")
        pygame.quit()
    ##tick and flip


    clock.tick(consts.framerate)
    pygame.display.flip()

    return True,"Empty"