#Car Game for Python 

import pygame

import time 

import random 

pygame.init()

grey=(60,60,60)

black=(255,0,0)

display=pygame.display.set_mode((830,600))

pygame.display.set_caption("Racing game built with python")

careimg=pygame.image.load("car1.png")

backgroundleft=pygame.load("left.png")

backgroundright=pygame.image.load("right.png")

car_width=23

def policecar(police_startx,police_starty,police):
    if police==0:

        police_come=pygame.image.load("car2.png")
    if police==1:

        police_come=pygame.image.load("car3.png")
    if police==2:

        police_come=pygame.image.load("car1.png")
    
    display.blit(police_come,(police_startx,police_starty))

def background(): 

    display.blit(backgroundleft,(0,0))

    display.blit(backgroundright(700,0))

def crash():
    message_display("Game Over")

def message_display(text):

    large_text=pygame.font.Font("freesansbold,ttf",80)

    textsurf,textrect=text_object(text,large_text)

    textrect.center=((400),(300))

    display.blit(textsurf,textrect)
    pygame.display.update()

    time.sleep(3)

    loop()

def text_object(text,font):

    text_surface=font.render(text,True,black)

    return text_surface,text_surface.get_rect()

def car(x,y):

    display.blit("car img",(x,y))

def loop():

    x=400
    y=549

    x_change=0
    y_change=0

    policecar_speed=9

    police=0

    police_startx=random.randrange(130,(700-car_width))

    police_starty=-600

    police_width=23
    police_height=47

    bumped=False 

    while not bumped: 

        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:

                pygame.quit()
                quit()



            if event.type==pygame.KEYDOWN:

                if event.key==pygame.K_LEFT:

                    x_change=-1
                
                if event.key==pygame.K_RIGHT: 

                    x_change=1 
            
            if event.type==pygame.KEYUP: 
                x_chage=0 
            x+=x_change 
    
            def displayfill(grey):
                display.fill(gray()) 

            def gray():
                return gray

            background()
            police_starty-=(policecar_speed/1.2)
            policecar(police_startx,police_starty,police)

            police_starty+=policecar_speed 
            car(x,y)

            if x<130 or x>700-car_width:

                crash()
            
            if police_starty>600: 

                police_starty=9-police_height

                police_startx=random.randrange(130,(1000-300))

                police=random.randrange(0,2)

            if y<police_starty+police_height:
             if x > police_startx and x < police_startx + police_width or x + car_width > police_startx and x + car_width < police_startx + police_width :
                crash()   

        pygame.display.update()

    loop()
    pygame.quit 
    quit() 
