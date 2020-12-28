#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     27/05/2015
# Copyright:   (c) user 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame
import time
pygame.init()
display_width=500
display_height=500
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("demo")
black=(0,0,0)
white=(100,10,10)
carimg=pygame.image.load("C:\\Users\\user\\Desktop\\castle.jpg")

carimg_width = 80
def car(x,y):
    gameDisplay.blit(carimg,(x,y))
def crash():
    message_display("you crash")
def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect=text_objects(text,largeText)
    TextRect.center=((display_width/2),(display_height)/2)
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    gameloop()
def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()
def gameloop():
         x=display_width*0.45
         y=display_height*0.8
         x_change=0
         y_change=0
         gameexit=False
         while not gameexit:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameexit=True
                print(event)
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        x_change=-5
                    if event.key==pygame.K_RIGHT:
                        x_change=5
                    if event.key==pygame.K_UP:
                        y_change=-5
                    if event.key==pygame.K_DOWN:
                        y_change=5
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                        x_change=0
                        y_change=0
                x+=x_change
                y+=y_change
                if x > display_width-carimg_width or x<0:
                    crash()
                    gameexit=True

            pygame.display.update()
            gameDisplay.fill(white)
            car(x,y)
gameloop()
pygame.quit()
quit()
