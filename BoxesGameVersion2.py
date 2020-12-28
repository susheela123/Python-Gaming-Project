

#----------------------------------------------------------------------
# Name:        DOTS AND BOXES GAME
# Purpose:     PROJECT
#
# Author:      SUSHEELA
#
# Created:     14/06/2015
# Copyright:   (c) user 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import pygame
import math
import easygui

import random
class BoxesGameVersion2():
    def initGraphics(self):
        self.normallinev=pygame.image.load("normalline.png")
        self.normallineh=pygame.transform.rotate(pygame.image.load("normalline.png"), -90)
        self.bar_donev=pygame.image.load("bar_done.png")
        self.bar_doneh=pygame.transform.rotate(pygame.image.load("bar_done.png"), -90)
        self.hoverlinev=pygame.image.load("hoverline.png")
        self.hoverlineh=pygame.transform.rotate(pygame.image.load("hoverline.png"), -90);

        self.separators=pygame.image.load("separators.png")
        self.redindicator=pygame.image.load("redindicator.png")
        self.greenindicator=pygame.image.load("greenindicator.png")
        self.greenplayer=pygame.image.load("greenplayer.png")
        self.blueplayer=pygame.image.load("blueplayer.png")
        self.winningscreen=pygame.image.load("youwin.png")
        self.gameover=pygame.image.load("gameover.png")
        self.score_panel=pygame.image.load("score_panel.png")
    def __init__(self):

        pass
        #1
        pygame.init()
        self.dimensions=int(input("enter the dimensions"))
        #pygame.font.init()
        self.turn=0
        width, height = 500,500
        self.boardh = [[False for x in range(self.dimensions)] for y in range(self.dimensions+1)]
        self.boardv = [[False for x in range(self.dimensions+1)] for y in range(self.dimensions)]
        self.box=[[0 for x in range(self.dimensions) ] for y in range(self.dimensions)]
        self.boxcount=[[0 for x in range(self.dimensions) ] for y in range(self.dimensions)]
        self.no_of_boxes=0
        #2
        #initialize the screen
        self.screen = pygame.display.set_mode((width, height))
        self.result=pygame.display.set_mode((width, height))
        pygame.display.set_caption("Boxes")
        #3
        #initialize pygame clock
        self.clock=pygame.time.Clock()
        self.initGraphics()
        self.me=0
        self.otherplayer=0
        self.didiwin=False
        #self.owner = [[0 for x in range(6)] for y in range(6)]
        self.xbox=0
        self.ybox=0
        self.newbox=0
        self.turn=0
        self.switch=0
        ##print "self.turn in init()",self.turn
        self.total=0




    def drawHUD(self):
    #draw the background for the bottom:

        #create font
        myfont = pygame.font.SysFont("freesansbold", 32)

        #create text surface
        label = myfont.render("Your Turn:", 1, (255,255,255))


        #draw surface
        #self.screen.blit(label, (35, 500))
        myfont64 = pygame.font.SysFont("freesansbold", 64)
        myfont20 = pygame.font.SysFont("freesansbold", 20)


        self.scoreme = myfont64.render(str(self.me), 1, (255,255,255))
        self.scoreother = myfont64.render(str(self.otherplayer), 1, (255,255,255))
        self.labelwin= myfont20.render("You win", 1, (255,255,255))
        self.computerwin=myfont20.render("computer win",1,(255,255,255))
        scoretextme = myfont20.render("You", 1, (255,255,255))
        scoretextother = myfont20.render("Other Player", 1, (255,255,255))
        self.screen.blit(self.score_panel,(650,10))
        self.screen.blit(scoretextme, (700, 10))
        self.screen.blit(self.scoreme, (700, 50))
        self.screen.blit(scoretextother, (900, 10))
        self.screen.blit(self.scoreother, (900, 50))
        self.screen.blit(self.greenindicator,(650,30))
        self.screen.blit(self.redindicator,(850,30))
    def drawBoard(self):
        for x in range(self.dimensions):
         for y in range(self.dimensions+1):
            if not self.boardh[y][x]:
                self.screen.blit(self.normallineh, [(x)*64+5, (y)*64])
            else:
                self.screen.blit(self.bar_doneh, [(x)*64+5, (y)*64])
        for x in range(self.dimensions+1):
         for y in range(self.dimensions):
            if not self.boardv[y][x]:
                self.screen.blit(self.normallinev, [(x)*64, (y)*64+5])
            else:
                self.screen.blit(self.bar_donev, [(x)*64, (y)*64+5])

        #draw separators
        for x in range(self.dimensions+1):
            for y in range(self.dimensions+1):
                self.screen.blit(self.separators, [x*64, y*64])
    def check_four(self):
        self.newbox=0
        ##print "self.turn in check_four:",self.turn
        for x in range(self.dimensions):
         for y in range(self.dimensions):

            if self.boardh[y][x] and self.boardv[y][x] and self.boardh[y+1][x] and self.boardv[y][x+1]:
                if self.box[y][x]==0:
                 if self.turn==1:
                    if self.box[y][x]=="G":
                        continue
                    else:
                        self.box[y][x]="B"



                        self.newbox+=1
                        #self.turn=0
                        self.no_of_boxes+=1

                        self.me+=1
                        self.turn=0

                        #print "your score",self.me
                        #print "you got another turn"


                 if self.turn==0:
                    if self.box[y][x]=="B":
                        continue
                    else:
                        self.box[y][x]="G"
                        #self.turn=1
                        self.no_of_boxes+=1

                        self.newbox+=1
                        #self.otherplayer+=1
                        #print "other player's turn"

                 #print "self.otherplayer",self.otherplayer






    def drawBox(self):
             ##print "enter drawBox"

             for x in range(self.dimensions):
                 for y in range(self.dimensions):

                    if self.box[y][x]=="B":


                        self.screen.blit(self.blueplayer, (x*64+5,y*64+5))
                        me=1


                    if self.box[y][x]=="G":

                         self.screen.blit(self.greenplayer, (x*64+5,y*64+5))
                         other=1






    def mouse_event(self):
                ##print "entered mouse_event"

                mouse = pygame.mouse.get_pos()
                crash=False

                pressed=0


                xpos = int(math.ceil((mouse[0]-32)/64.0))
                ypos = int(math.ceil((mouse[1]-32)/64.0))


                is_horizontal = abs(mouse[1] - ypos*64) < abs(mouse[0] - xpos*64)


                ypos = ypos - 1 if mouse[1] - ypos*64 < 0 and not is_horizontal else ypos
                xpos = xpos - 1 if mouse[0] - xpos*64 < 0 and is_horizontal else xpos


                board=self.boardh if is_horizontal else self.boardv
                isoutofbounds=False


                try:
                      if not board[ypos][xpos]: self.screen.blit(self.hoverlineh if is_horizontal else self.hoverlinev, [xpos*64+5 if is_horizontal else xpos*64, ypos*64 if is_horizontal else ypos*64+5])
                except:
                      isoutofbounds=True
                pass
                if not isoutofbounds:
                       alreadyplaced=board[ypos][xpos]
                else:
                       alreadyplaced=False




                if pygame.mouse.get_pressed()[0] and not alreadyplaced and not isoutofbounds:

                       if is_horizontal:
                         self.boardh[ypos][xpos]=True
                       else:
                        self.boardv[ypos][xpos]=True
                       if self.turn==0:
                         self.turn=1

                       else:                                                            ##print "turn changed",self.turn
                          self.turn=0
                       if is_horizontal:
                        if ypos>0:
                            self.boxcount[ypos-1][xpos]+=1
                        if ypos<self.dimensions:
                            self.boxcount[ypos][xpos]+=1
                       else:
                        if xpos>0:
                            self.boxcount[ypos][xpos-1]+=1
                        if xpos<self.dimensions:
                            self.boxcount[ypos][xpos]+=1
                       #print "self.boxcount in mouseclick():",self.boxcount







                self.check_four()
                ##print "entered user drawbox()"


                self.drawBox()



                pygame.display.flip()





    #computer move
    def computermove(self):
            print ("computermove()")
            self.takesafe3s()

            if self.sides3()==True:#sides3 uses u,v
                print ("sides03 exist")
                if self.sides01()==True:#sides01 uses x,y
                    print ("sides3 TRUE sides01 TRUE ")
                    self.takeall3s()#takeall3s() uses u,v
                    self.takeedge()#takeedge() uses x,y,z

                else:
                    print ("sides3 TRUE sides01 FALSE")
                    self.takeall3s()
                    self.makeanymove()
                if self.me+self.otherplayer==self.dimensions*self.dimensions:
                           #print "your score:",self.me
                           #print "other player score",self.otherplayer
                           if self.me>self.otherplayer:
                                        print ("you win")
                                        #self.result.blit(self.winningscreen, [0,0])
                                        self.screen.blit(self.labelwin,(650,300))
                                        easygui.msgbox("You win")
                           elif self.me==self.otherplayer:
                                        print ("Draw")
                                    #    self.result.blit(self.gameover, [0,0])
                                        self.screen.blit(self.computerwin,(650,100))
                                        easygui.msgbox("Draw")
                           else:
                                        print ("you lose")
                                        easygui.msgbox("You lose")

                           self.update()
            elif self.sides01()==True:
                print ("sides01 TRUE")
                self.takeedge()
            elif self.singleton()==True:
                print ("singleton TRUE")
                self.takeedge()
            elif self.doubleton()==True:
                print ("Doubleton")
                self.takeedge()
            else:
                print ("makeanymove")
                self.makeanymove()
            print ("end of computermove()")



    #takesafe3s function
    def takesafe3s(self):
        print ("entered takesafe3s()")
        for i in range(0,self.dimensions):
            for j in range(0,self.dimensions):
                if self.boxcount[i][j]==3:
                    if self.boardv[i][j]==False:
                        if j==0 or self.boxcount[i][j-1]!=2:
                            print ("set the positions safely")
                            self.x=i
                            self.y=j
                            #print "called setvedge()"
                            self.setvedge()
                    elif self.boardh[i][j]==False:
                        if i==0 or self.boxcount[i-1][j]!=2:
                            print ("set the positions safely")
                            self.x=i
                            self.y=j
                            #print "called sethedge()"
                            self.sethedge()

                    elif self.boardv[i][j+1]==False:
                        if j==self.dimensions-1 or self.boxcount[i][j+1]!=2:
                            print ("set the positions safely")
                            self.x=i
                            self.y=j+1
                            #print "setvedge()"
                            self.setvedge()
                    elif self.boardh[i+1][j]==False:
                        if i==self.dimensions-1 or self.boxcount[i+1][j]!=2:
                            print ("set the positions safely")
                            self.x=i+1
                            self.y=j
                            #print "sethedge()"
                            self.sethedge()
        print ("takesafe3s() exit")
    #sethedge()
    def sethedge(self):
        #print "entered sethedge() with self.x and self.y values as: ",self.x,self.y
        self.boardh[self.x][self.y]=True

        if self.x>0:
            self.boxcount[self.x-1][self.y]+=1
        if self.x<self.dimensions:
            self.boxcount[self.x][self.y]+=1
        #print "self.boxcount in sethedge:",self.boxcount
        #print "self.boardh,",self.boardh
        self.screen.blit(self.hoverlineh,(self.x*64+5,self.y*64))
        self.checkh()
        if self.me+self.otherplayer==self.dimensions*self.dimensions:
            self.update()
        self.turn=1-self.turn

    #setvedge
    def setvedge(self):
        #print "entered setvedge with self.x and self.y as ",self.x,self.y
        self.boardv[self.x][self.y]=True
        if self.y>0:
            self.boxcount[self.x][self.y-1]+=1
        if self.y<self.dimensions:
            self.boxcount[self.x][self.y]+=1
        self.screen.blit(self.hoverlinev,(self.x*64,self.y*64+5))
        self.checkv()
        if self.me+self.otherplayer==self.dimensions*self.dimensions:
            self.update()
        self.turn=1-self.turn

    #checkh()
    def checkh(self):
        #print "entered checkh() with self.x and self.y as,",self.x,self.y
        hit=0
        if self.x>0:
            if self.boxcount[self.x-1][self.y]==4 :
                #print "color box"
                self.box[self.x-1][self.y]="G"
                #self.drawBox()
                self.screen.blit(self.greenplayer, (self.x*64+5,self.y*64+5))
                self.otherplayer+=1
                hit=1
        if self.x<self.dimensions:
            if self.boxcount[self.x][self.y]==4 :
                #print "color box"
                self.box[self.x][self.y]="G"
                #self.drawBox()
                self.screen.blit(self.greenplayer, (self.x*64+5,self.y*64+5))
                self.otherplayer+=1
                hit=1
        #print "computer score:",self.otherplayer
        if hit>0:
          if self.me+self.otherplayer<self.dimensions*self.dimensions:

            self.turn=1-self.turn

    #checkv()
    def checkv(self):

        #print "entered checkv() with self.x and self.y as",self.x,self.y
        hit=0
        if self.y>0:
            if self.boxcount[self.x][self.y-1]==4 :
                #print "color box"
                self.box[self.x][self.y-1]="G"
                self.screen.blit(self.greenplayer, (self.x*64+5,self.y*64+5))
                self.otherplayer+=1
                hit=1
        if self.y<self.dimensions:
            if self.boxcount[self.x][self.y]==4 :
                #print "color box"
                self.box[self.x][self.y]="G"
                self.screen.blit(self.greenplayer, (self.x*64+5,self.y*64+5))
                self.otherplayer+=1
                hit=1
        #print "computer score:",self.otherplayer
        if hit>0:
          if self.me+self.otherplayer<self.dimensions*self.dimensions:

            self.turn=1-self.turn

    #sides3()
    def sides3(self):
        #print "sides3()"
        #print "#print boxcount: in sides03():",self.boxcount

        for i in range(0,self.dimensions):
            for j in range(0,self.dimensions):
                if self.boxcount[i][j]==3:
                    self.u=i
                    self.v=j

                    return True
        return False
    #sides01()
    def sides01(self):
            #print "entered sides01"
            self.x=0
            self.y=0
            self.z=random.randint(1,2)
            is_horizontal=False
            is_vertical=False
            if self.z==1:
                # #print "self.z=1"
                 self.x=random.randint(0, self.dimensions)
                 self.y=random.randint(0,self.dimensions-1)
                 ##print "entering into self.randhedge"
                 if self.randhedge()==True:
                    return True

                 else:
                    self.z=2
                    self.x=random.randint(0, self.dimensions-1)
                    self.y=random.randint(0,self.dimensions)
                    if self.randvedge()==True:
                       return True
            else:
               # #print "self.z==2"
                self.x=random.randint(0, self.dimensions-1)
                self.y=random.randint(0,self.dimensions)
               # #print "entering into self.randvedge"
                if self.randvedge()==True:
                    return True

                else:
                    self.z=1
                    self.x=random.randint(0, self.dimensions)
                    self.y=random.randint(0,self.dimensions-1)
                    #print "entered into self.randhedge2"
                    if self.randhedge()==True:
                        return True
            return False
    #randhedge()
    def randhedge(self):
            m=self.x
            n=self.y
            #print "entered randhedge"
            ##print "self.x,self.y before callinf safehedge for 1st time"
            if self.safehedge():
                return True
            else:
                self.y+=1
                if self.y==self.dimensions:
                    self.y=0
                    self.x+=1
                    if self.x>self.dimensions:
                        self.x=0
            while self.x!=m or self.y!=n:
                #print "self.x,self.y before calling safehedge:",self.x,self.y
                if self.safehedge():
                    return True
                else:
                    self.y+=1
                    #print "self.y:",self.y
                    if self.y==self.dimensions:
                        self.y=0
                        self.x+=1
                        #print "self.x:",self.x
                        if self.x>self.dimensions:
                            #print "self.x=>"
                            self.x=0
            return False
    #randvedge()
    def randvedge(self):
            m=self.x
            n=self.y
            #print "entered randvedge() with self.x and self.y as,",self.x,self.y
            if self.safevedge():
                return True
            else:
                self.y+=1
                if self.y>self.dimensions:
                    self.y=0
                    self.x+=1
                    if self.x==self.dimensions:
                        self.x=0
            while self.x!=m or self.y!=n:
                if self.safevedge():
                    return True
                else:
                    self.y+=1
                    if self.y>self.dimensions:
                        self.y=0
                        self.x+=1
                        if self.x==self.dimensions:
                            self.x=0
            return False
    #safehedge()
    def safehedge(self):
            #print "entered safehedge with self.x and self.y as,",self.x,self.y

            if self.boardh[self.x][self.y]==False:

                if self.x==0:
                    if self.boxcount[self.x][self.y]<2:
                        #print "safehedge returns TRUE"
                        return True
                elif self.x==self.dimensions:
                    if self.boxcount[self.x-1][self.y]<2:
                        #print "safehedge returns TRUE"
                        return True
                elif self.boxcount[self.x][self.y]<2 and self.boxcount[self.x-1][self.y]:
                    #print"safehedge returns TRUE"
                    return True
            #print"safehedge returns FALSE"
            return False
    #safevedge()
    def safevedge(self):
            #print "entered safevedge with self.x and self.y as, ",self.x,self.y
            if self.boardv[self.x][self.y]==False:
                if self.y==0:
                    #print "self.x,self.y",self.x,self.y
                    if self.boxcount[self.x][self.y]<2:
                        return True
                elif self.y==self.dimensions:
                    if self.boxcount[self.x][self.y-1]<2:
                        return True
                elif self.boxcount[self.x][self.y]<2 and self.boxcount[self.x][self.y-1]<2:
                    return True
            return False
    #takeall3s()
    def takeall3s(self):
        #print "entered takeall3s"
        while self.sides3():
            #print "in take all 3s() sides3()==True"
            self.takebox()
        #print "left takeall3s"
    #takebox()
    def takebox(self):
        self.e=self.x
        self.f=self.y
        #print"entered takebox with self.u self.v",self.u,self.v
        if self.boardh[self.u][self.v]==False:
            self.x=self.u
            self.y=self.v
            #print "sethedge() with self.x and self.y as",self.x,self.y
            self.sethedge()

        elif self.boardv[self.u][self.v]==False:
            self.x=self.u
            self.y=self.v
            #print "setvedge() with self.x and self.y as",self.x,self.y
            self.setvedge()
        elif self.boardh[self.u+1][self.v]==False:
            self.x=self.u+1
            self.y=self.v
            #print "sethedge() with self.x and self.y as",self.x,self.y
            self.sethedge()
        elif self.boardv[self.u][self.v+1]==False:
            self.x=self.u
            self.y=self.v+1
            #print "setvedge() with self.x and self.y as",self.x,self.y
            self.setvedge()
        self.x=self.e
        self.y=self.f
        #print "left takebox()"
    #takeedge
    def takeedge(self):
        #print "entered takeedge() with self.x and self.y as",self.x,self.y
        if self.z==2:
            #print "setvedge() with self.x and self.y as",self.x,self.y
            self.setvedge()
        elif self.z==1:
            #print "sethedge() with self.x and self.y as",self.x,self.y
            self.sethedge()
        #print "left takedge()"
    #incount
    def incount(self):
            ##print "incount"
            #print "self.u and self.v",self.u,self.v



            self.count=self.count+1
            if self.k!=1 and self.boardv[self.u][self.v]==False:
                if self.v>0:
                    if self.boxcount[self.u][self.v-1]>2:
                        self.count+=1
                        self.loop=True
                    elif self.boxcount[self.u][self.v-1]>1:
                        self.k=3
                        self.v=self.v-1
                        self.incount()
            elif self.k!=2 and self.boardh[self.u][self.v]==False:
                if self.u>0:
                    if self.boxcount[self.u-1][self.v]>2:
                        self.count+=1
                        self.loop=True
                    elif self.boxcount[self.u-1][self.v]>1:
                        self.k=4
                        self.u=self.u-1
                        self.incount()
            elif self.k!=3 and self.boardv[self.u][self.v+1]==False:
                if self.v<self.dimensions-1:
                    if self.boxcount[self.u][self.v+1]>2:
                        self.count+=1
                        self.loop=True
                    elif self.boxcount[self.u][self.v+1]>1:
                        self.k=1
                        self.v=self.v+1
                        self.incount()
            elif self.k!=4 and self.boardh[self.u+1][self.v]==False:
                if self.u<self.dimensions-1:
                    if self.boxcount[self.u+1][self.v]>2:
                        self.count+=1
                        self.loop=True
                    elif self.boxcount[self.u+1][self.v]>1:
                        self.u==self.u+1
                        self.k=2
                        self.incount()
            #print "count: at end of incount():",self.count

    #sac()
    def sac(self):
            #print "entered sac"
            self.count=0
            self.loop=False
            self.k=0
            self.incount()
            print ("count:",self.count)
            if self.loop==False:
                self.takeallbut()
            if self.count+self.me+self.otherplayer==self.dimensions*self.dimensions:

                self.takeall3s()
            else:
                if self.loop==True:
                    self.count=self.count-2
                self.k=0
                self.outcount()
                self.u=self.dimensions
                self.v=self.dimensions
            #print "left sac()"
    #incount()

    #takeallbut()
    def takeallbut(self):
        #print "entered takeallbut()"
        while self.sides3not():
            self.takebox()
        #print "left takeallbut"
    #sides3not()
    def sides3not(self):
        #print "entered sides3not()"
        for i in range(0,self.dimensions):
            for j in range(0,self.dimensions):
                if self.boxcount[i][j]==3:
                    if i!=self.u or j!=self.v:
                        self.u=i
                        self.v=j
                        #print "left sides3not()"
                        return True
        #print "left sides3not()"
        return False
    #outcount()
    def outcount(self):
            #print "entered outcount"
            if self.count>0:
                if self.k!=1 and self.boardv[self.u][self.v]==False:
                    if self.count!=2:
                     self.x=self.u
                     self.y=self.v
                     self.setvedge()


                    self.count=self.count-1
                    self.k=3
                    self.v=self.v-1
                    self.outcount()
                if self.k!=2 and self.boardh[self.u][self.v]==False:
                    if self.count!=2:
                        self.x=self.u
                        self.y=self.v
                        self.sethedge()


                    self.count=self.count-1
                    self.k=4
                    self.u=self.u-1
                    self.outcount()
                if self.k!=3 and self.boardv[self.u][self.v+1]==False:
                    if self.count!=2:
                        self.x=self.u
                        self.y=self.v+1
                        self.setvedge()



                    self.count=self.count-1
                    self.k=1
                    self.v=self.v+1
                    self.outcount()
                if self.k!=4 and self.boardh[self.u+1][self.v]==False:
                    if self.count!=2:
                        self.x=self.u+1
                        self.y=self.v
                        sethedge(self.u+1,self.v)


                    self.count=self.count-1
                    self.k=2
                    self.u=self.u+1
                    self.outcount()
            #print "left outcount()"
    #singleton()
    def singleton(self):
            print ("entered singleton")
            for i in range(0,self.dimensions):
                for j in range(0,self.dimensions):
                    if self.boxcount[i][j]==2:
                        numb=0
                        if self.boardh[i][j]==False:
                            if i<1 or self.boxcount[i-1][j]<2:
                                numb+=1
                        self.z=2
                        if self.boardv[i][j]==False:
                            if j<1 or self.boxcount[i][j-1]<2:
                                numb+=1
                            if numb>1:
                                self.x=i
                                self.y=j
                                return True
                        if self.boardv[i][j+1]==False:
                            if j+1==self.dimensions or self.boxcount[i][j+1]<2:
                                numb+=1
                            if numb>1:
                                self.x=i
                                self.y=j+1
                                return True
                        self.z=1
                        if self.boardh[i+1][j]==False:
                            if i+1==self.dimensions or self.boxcount[i+1][j]<2:
                                numb+=1
                            if numb>1:
                                self.x=i+1
                                self.y=j
                                return True
            return False
    #doubleton()
    def doubleton(self):
            print ("entered doubleton")
            self.z=2
            for i in range(0,self.dimensions):
                for j in range(0,self.dimensions-1):
                    if self.boxcount[i][j]==2 and self.boxcount[i][j+1]==2 and self.boardv[i][j+1]==False:
                        self.k=i
                        self.l=j
                        if self.ldub() and self.rdub():
                            self.x=self.k
                            self.y=self.l+1
                            print ("self.x and self.y in doubleton:",self.x,self.y)
                            return True
            self.z=1
            for j in range(0,self.dimensions):
                for i in range(0,self.dimensions-1):
                    if self.boxcount[i][j]==2 and self.boxcount[i+1][j]==2 and self.boardh[i+1][j]==False:
                        self.k=i
                        self.l=j
                        if self.udub() and self.ddub():
                            self.x=self.k+1
                            self.y=self.l
                            print ("self.x and self.y in doubleton:",self.x,self.y)
                            return True
            return False
    #ldub()
    def ldub(self):
            #print "entered ldub"
            if self.boardv[self.k][self.l]==False:
                if self.l<1 or self.boxcount[self.k][self.l-1]<2:
                    return True
            elif self.boardh[self.k][self.l]==False:
                if self.k<1 or self.boxcount[self.k-1][self.l]<2:
                    return True
            elif self.k==self.dimensions or self.boxcount[self.k-1][self.l]<2:
                return True
            return False
    def rdub(self):
            #print "entered rdub"
            if self.boardv[self.k][self.l+1+1]==False:
                if self.k+1+1==self.dimensions or self.boxcount[self.k][self.l+1]<2:
                    return True
            elif self.boardh[self.k][self.l+1]==False:
                if self.k<1 or self.boxcount[self.k-1][self.l+1]<2:
                    return True
            elif self.k+1==self.dimensions or self.boxcount[self.k+1][self.l+1]<2:
                return True
            return False
    def udub(self):
            #print "entered udub"
            if self.boardh[self.k][self.l]==False:
                if self.k<1 or self.boxcount[self.k-1][self.l]<2:
                    return True
            elif self.boardv[self.k][self.l]==False:
                if self.l<1 or self.boxcount[self.k][self.l-1]<2:
                    return True
            elif self.l==self.dimensions-1 or self.boxcount[self.k][self.l+1]<2:
                return True
            return False
    def ddub(self):
            #print "entered ddub"
            if self.boardh[self.k+1+1][self.l]==False:
                if self.k+1==self.dimensions-1 or self.boxcount[self.k+1][self.l]<2:
                    return True
            elif self.boardv[self.k+1][self.l]==False:
                if self.l<1 or self.boxcount[self.k+1][self.l-1]<2:
                    return True
            elif self.l==self.dimensions-1 or self.boxcount[self.k+1][self.l+1]<2:
                return True
            return False
    #makeanymove()
    def makeanymove(self):
        #print "entered makeanymove()"
        self.x=-1
        for i in range(0,self.dimensions+1):
            for j in range(0,self.dimensions):
                #print "self.x and self.y in makeanymove as",self.x,self.y
                #print
                #print "self.boardh[i][j]",self.boardh


                if self.boardh[i][j]==False:
                    self.x=i
                    self.y=j
                    i=self.dimensions+1
                    j=self.dimensions
                    break
        if self.x<0:
                    for i in range(0,self.dimensions):
                        for j in range(0,self.dimensions+1):
                            #print "self.x and self.y in makeanymove as",self.x,self.y
                            #print "self.boardv[i][j]: for dimensions",self.boardv,self.dimensions
                            if self.boardv[i][j]==False:
                                self.x=i
                                self.y=j
                                i=self.dimensions
                                j=self.dimensions+1
                    self.setvedge()
        else:
                    self.sethedge()
        if self.turn==1 and self.me+self.otherplayer<self.dimensions*self.dimensions:
                    self.computermove()









































    def update(self):
        ##print "entered update()"
        #sleep to make the game 60 fps
        #self.clock.tick(60)
        white=(240,100,50)
        white1=(255,255,255)
        black=(0,0,0)
        #clear the screen
        self.screen.fill(white)
        self.drawBoard()
        self.drawHUD()
        crashed=False
       # #print "self.turn in update",self.turn


        if self.me+self.otherplayer==self.dimensions*self.dimensions:
            #self.drawBox()
            self.result="you scored "+str(self.me)+" computer scored "+str(self.otherplayer)


            myfont64 = pygame.font.SysFont("", 64)
            myfont20 = pygame.font.SysFont("", 20)

            self.scoreme = myfont64.render(str(self.me), 1, (255,255,255))
            self.scoreother = myfont64.render(str(self.otherplayer), 1, (255,255,255))
            self.screen.blit(self.scoreme, (700, 50))
            self.screen.blit(self.scoreother, (900, 50))
            #print "your score:",self.me
            #print "other player score",self.otherplayer
            if self.me>self.otherplayer:
                        #print "you win"
                        #self.result.blit(self.winningscreen, [0,0])
                        self.screen.blit(self.labelwin,(650,300))
                        easygui.msgbox("You win")
            elif self.me==self.otherplayer:
                        #print "Draw"
                        #self.result.blit(self.gameover, [0,0])
                        self.screen.blit(self.computerwin,(650,100))
                        easygui.msgbox("Draw")
            else:
                        #print "you lose"
                        easygui.msgbox("computer wins")
                        easygui.msgbox(str(self.result))

            pygame.quit()
            quit()









        for event in pygame.event.get():
                #quit if the quit button was pressed
                if event.type == pygame.QUIT:
                    if self.me>self.otherplayer:
                        #print "you win"
                        #self.result.blit(self.winningscreen, [0,0])
                        easygui.msgbox("You win")
                    elif self.me==self.otherplayer:
                        #print "Draw"
                        #self.result.blit(self.gameover, [0,0])
                        easygui.msgbox("Draw")
                    else:
                        #print "you lose"
                        easygui.msgbox("computer wins")
                    crashed=True

                    pygame.quit()
                    quit()

                #jhturn=self.mouse_event()
        ##print "mouse_event is called"
        if self.turn==0:

            self.mouse_event()
            ##print "got back to update after mouse event"
        elif self.turn==1:
            self.computermove()
       # #print "mouse_event is returned"
        #self.drawBox()








bg=BoxesGameVersion2() #__init__ is called right here
while 1:
    bg.update()



