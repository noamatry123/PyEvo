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
myfont =pygame.font.SysFont("Ariel", 30)
myfont1=pygame.font.SysFont("Ariel", 30)
myfont2=pygame.font.SysFont("Ariel", 20)
last_clickcheck=None

def printAtt(playerCell):
    counter=0
    for att in playerCell.getUsefullAtts():
        label = myfont.render(att,1, (0,0,0))
        screen.blit(label, (0,counter))
        counter+=30
def askBoard(mode, text,option1="",option2="",text2=""):
    Button1 = Buttons.Button()
    Button2 = Buttons.Button()
    screen.fill((255,0,255))

    screencenter=(consts.screenwidth/2-100,consts.screenheight/2-100)
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
    if mode=="manualAuto":
        ptext=text.split("\n")
        ptext2=text2.split("\n")
        ptext.remove("")
        ptext2.remove("")
        plabel=[]
        plabel2=[]
        color1=(0,0,0)
        color2=(0,0,0)
        pt1=""
        pt2=""
        for p,p2 in zip(ptext,ptext2):
            pt1=p[p.find(":")+1:len(p)]
            pt2=p2[p2.find(":")+1:len(p2)]
            if p in ["new","old"]:
                    color1=(0,0,0)
                    color2=(0,0,0)
            #bad if bigger
            elif p[0:p.find(":")]in ["timeToLay","eggHatchTime","eggwithdraw"]:
                if int(pt1)>int(pt2):
                    color1=(255,0,0)
                    color2=(0,255,0)
                elif int(pt1)<int(pt2):
                    color1=(0,255,0)
                    color2=(255,0,0)
                else:
                    color1=(0,0,0)
                    color2=(0,0,0)
            #bad if smaller
            else:
                if int(pt1)>int(pt2):
                    color1=(0,255,0)
                    color2=(255,0,0)
                elif int(pt1)<int(pt2):
                    color1=(255,0,0)
                    color2=(0,255,0)
                else:
                    color1=(0,0,0)
                    color2=(0,0,0)
            plabel.append(myfont1.render(p, 1, color1))
            plabel2.append(myfont1.render(p2, 1, color2))
        for i in range(0,len(plabel)):
            screen.blit(plabel[i],(screencenter[0]-(screencenter[0]/2+screencenter[0]/4),10+i*25))
        for i in range(0,len(plabel2)):
            screen.blit(plabel2[i],(screencenter[0]+(screencenter[0]/2+screencenter[0]/4),10+i*25))
        #Parameters:          surface,      color,       x,                         y,              length, height, width,       text,      text_color
        Button1.create_button(screen, (107,142,35), (screencenter[0]),80,         100,    100,    0,        option1, (255,255,255))
        Button2.create_button(screen, (107,142,35), (screencenter[0]), 80+100+40, 100,    100,    0,        option2, (255,255,255))
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
    ##fill screen / season
    if consts.season==0:
        screen.fill((255,255,0))
    elif consts.season==1:
        screen.fill((236,39,39))
    elif consts.season==2:
        screen.fill((213,244,252))
    elif consts.season==3:
        screen.fill((252,88,181))
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
            color=(0,0,0)
            if cell.mode=="c":
                color=(255,0,0)
            label = myfont2.render(str(cell.ID), 1, color)
            screen.blit(label,(cell.location.x+5,cell.location.y))
            ##draw life:
            label = myfont2.render(str(cell.lifeTimeLeft), 1, (0,0,0))
            screen.blit(label,(cell.location.x-15,cell.location.y))
            pygame.draw.rect(screen,(255,0,0),(cell.location.x-10,cell.location.y-15,(30*(cell.lifeTimeLeft/float(cell.lifeTime))),6))

    for food in foodList:
        #pygame.draw.circle(screen,(80,255,80),(food.location.getTupple()),food.rad)
        screen.blit(food.image,(food.location.x-food.rad,food.location.y-food.rad))
    ##prints attributes
    printAtt(playerCell)
    ##draw player eggs
    for egg in eggList[0]:
        screen.blit(egg.image,(egg.location.x-egg.rad,egg.location.y-egg.rad))
        #pygame.draw.circle(screen,(255,255,255),(egg.location.getTupple()),egg.rad)
    for egg in eggList[1]:
        screen.blit(egg.image,(egg.location.x-egg.rad,egg.location.y-egg.rad))
        #pygame.draw.circle(screen,(255,255,255),(egg.location.getTupple()),egg.rad)
    ##draw player
    ##pygame.draw.circle(screen,(0,0,0),(playerCell.location.getTupple()),playerCell.rad)
    ##pygame.draw.circle(screen,(10,255,10),(playerCell.location_compensated()),2)
    if playerCell.timeToHurt%2==0:
        screen.blit(playerCell.image,(playerCell.location.x-playerCell.rad,playerCell.location.y-playerCell.rad))
        pygame.draw.rect(screen,(255,0,0),(playerCell.location.x-10,playerCell.location.y-15,(30*(playerCell.lifeTimeLeft/float(playerCell.lifeTime))),6))
        ##draw player ID
        label = myfont2.render(str(playerCell.ID), 1, (255,255,0))
        screen.blit(label,(playerCell.location.x,playerCell.location.y))
    ##tick and flip


    clock.tick(consts.framerate)
    pygame.display.flip()

    return True,"Empty"