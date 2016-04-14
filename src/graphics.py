__author__ = 'user-pc'
import pygame
import time
import classes
import math
import termcolor
import easygui
import consts
import Buttons
import dumbmenu as dm
screen=None
clock=None
myfont =pygame.font.SysFont("Ariel", 30)
myfont1=pygame.font.SysFont("Ariel", 30)
myfont2=pygame.font.SysFont("Ariel", 20)
practicleList=[]
last_clickcheck=None

def printAtt(playerCell):
    counter=0
    for att in playerCell.getUsefullAtts():
        label = myfont.render(att,1, (0,0,0))
        screen.blit(label, (0,counter))
        counter+=30
def askBoard(mode, text="",option1="",option2="",text2=""):
    Button1 = Buttons.Button()
    Button2 = Buttons.Button()
    screencenter=(consts.screenwidth/2-100,consts.screenheight/2-100)
    screencenter_below=(consts.screenwidth/2-100,(consts.screenheight/2+(consts.screenheight/4)))

    if mode=="menu":
        t=["New Game","Godmode: Off","Recording: On","Controls: Mouse","What keys can i press?","Start game","Quit"]
        choose=-1
        while(choose!=5 and choose!=6):
            screen.fill((0,0,0))
            choose = dm.dumbmenu(screen, [
                            t[0],
                            t[1],
                            t[2],
                            t[3],
                            t[4],
                            t[5],t[6]], 64,64,None,32,1.4,(0,255,0),(255,0,0))

            if choose == 0:
                #New / Load
                if consts.loadedGame==False:
                    consts.loadedGame=True
                    t[0]="Loaded Game"
                else:
                    consts.loadedGame=False
                    t[0]="New Game"
                print consts.loadedGame
            elif choose == 1:
                #Godmode
                if consts.godmode==False:
                    consts.godmode=True
                    t[1]="Godmode: On"
                else:
                    consts.godmode=False
                    t[1]="Godmode: Off"
            elif choose == 2:
                #New / Load
                if consts.recording==True:
                    consts.recording=False
                    t[2]="Recording: Off"
                else:
                    consts.recording=True
                    t[2]="Recording: On"
            elif choose == 3:
                #New / Load
                if consts.mouse_control==True:
                    consts.mouse_control=False
                    t[3]="Controls: Keyboard"
                else:
                    consts.mouse_control=True
                    t[3]="Controls: Mouse"
            elif choose == 4:
                text=" \n \n \n \nA = Lay egg\nC = Toggle carnivore and mating modes\nM = Pause menu (save game)\n"
                if consts.mouse_control==True:
                    text+="Left click = Move\nMove mouse = Change angle"
                else:
                    text+="Keyboard Arrows = Move and change angle"
                while(askBoard("Prompt",text)!="Okay"):
                    pass
                screen.fill((0,0,0))
            elif choose == 6:
                pygame.quit()
                exit()
            clock.tick(consts.framerate)
            pygame.display.flip()
        print consts.loadedGame

    ##switch mode
    if mode=="Prompt":
        screen.fill((255,0,255))
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
        screen.fill((255,0,255))
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
        screen.fill((255,0,255))
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
    seasoncolor=[(255,255,0),(236,39,39),(213,244,252),(252,88,181)]
    seasonid=0
    if consts.season==0:
        screen.fill(seasoncolor[0])
        seasonid=0
    elif consts.season==1:
        screen.fill(seasoncolor[1])
        seasonid=1
    elif consts.season==2:
        screen.fill(seasoncolor[2])
        seasonid=2
    elif consts.season==3:
        screen.fill(seasoncolor[3])
        seasonid=3
    ##handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False,"End"

    ##draw line for mouse "debugging"
    pygame.draw.aaline(screen, (30,30,30), (playerCell.location.x,playerCell.location.y), (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))
    pygame.draw.circle(screen, (255,50,50), (playerCell.location.x,playerCell.location.y),30)
    pygame.draw.circle(screen, seasoncolor[seasonid], (playerCell.location.x,playerCell.location.y),29)
    #pygame.draw.aaline(screen, (30,30,255), (playerCell.location.x,playerCell.location.y-30),(playerCell.location.x,playerCell.location.y+30))
    pygame.draw.aaline(screen, (30,30,255), (playerCell.location.x-30,playerCell.location.y),(playerCell.location.x+30,playerCell.location.y))
    pygame.draw.aaline(screen, (30,30,255), (playerCell.location.x-12,playerCell.location.y+28),(playerCell.location.x+12,playerCell.location.y-28))
    pygame.draw.aaline(screen, (30,30,255), (playerCell.location.x-12,playerCell.location.y-28),(playerCell.location.x+12,playerCell.location.y+28))
    pygame.draw.aaline(screen, (30,30,255), (playerCell.location.x+21,playerCell.location.y-21),(playerCell.location.x-21,playerCell.location.y+21))
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
            ##draw foodbar
            pygame.draw.rect(screen,(0,255,0),(cell.location.x-10,cell.location.y-6-15,(30*(cell.foodLeft/float(cell.lifeTime))),6))

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
        #foodbar
        pygame.draw.rect(screen,(0,255,0),(playerCell.location.x-10,playerCell.location.y-6-15,(30*(playerCell.foodLeft/float(playerCell.lifeTime))),6))
    ##draw practicles
    for practicle in practicleList:
        color=(practicle.color[0],practicle.color[1],practicle.color[2],85)
        pygame.draw.circle(screen,color,(practicle.loc.x,practicle.loc.y),practicle.radius)




    ##tick and flip
    clock.tick(consts.framerate)
    pygame.display.flip()

    return True,"Empty"