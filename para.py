import pygame, sys, pygame.mixer
from random import randint
from pygame.locals import *

pygame.init()
"""_____COLOURS_____"""
black = (0,0,0)
white = (255,255,255)
green = (152,251,152)
red = (255,0,0)
yellow=(255,250,205)
grey = (139,137,137)
brown = (139,119,101)
blue = (106,90,205)


"""_____SOUNDS______"""
fly = pygame.mixer.Sound("sound/fly.wav")
end = pygame.mixer.Sound("sound/End.wav")
crash = pygame.mixer.Sound("sound/crash.wav")


"""_____SCREEN & BACKGROUND____"""
sizex = 800
sizey = 600
size = sizex,sizey
looptimes = 1000
introbg_org = pygame.image.load("pic/introbg.png")
introbg = pygame.transform.scale(introbg_org,size)
background_org = pygame.image.load('pic/BG.jpg')
bglength=int(1000.0*float(sizey)/500.0)
background = pygame.transform.scale(background_org, (bglength,sizey))
background_org1 = 0.0
background_org2 = float(bglength)
backgroung_setorg2 = float(bglength)
background_speed = -float(bglength)/(2*looptimes)
SBbg_org = pygame.image.load("pic/SBbg.png")
SBbg = pygame.transform.scale(SBbg_org,size)
SB_org = pygame.image.load("pic/SB.png")
SB = pygame.transform.scale(SB_org,(700,450))


"""_____ABOUNT BIRD____"""
bird = pygame.image.load('pic/bird50.png')
birdsize = (50,50)
x_org = sizex/2
y_org = sizey/2
x_speed_org = 0
y_speed_org = 3
y_speed_up = -10
y_speed_down = 5


"""_____ANIME_____"""
nBird_org = pygame.image.load("pic/nice.png")
nBird = pygame.transform.scale(nBird_org,birdsize)
aBird_org = pygame.image.load("pic/angry.png")
aBird = pygame.transform.scale(aBird_org,birdsize)



"""_____ABOUT SUN & MOON_____"""
sun_org = pygame.image.load('pic/sun.png')
sun = pygame.transform.scale(sun_org, (110,110))
moon = pygame.image.load('pic/moon.png')
xsun_org = 200.0
ysun_org = 0
mod_org = 'DAY'
xsun_speed = 0.5
looptimes = looptimes


"""_____ABOUT PIPE AND OTHER OBSTACLE_____"""
pipeup = pygame.image.load('pic/fpipe.png')
pipedown = pygame.image.load('pic/pipe.png')
ceiling_org = 0
ground_org = sizey
space_org = 150
xloc_org = sizex
yloc_org = 0
xsize_org = 98
ysize_org = randint(0,sizey-space_org)
obspeed = 2.5



"""_____ABOUNT SCORE_____"""
score_org = 0
TOPNUMBER = 5
fps = 60
bolt = pygame.image.load("pic/bolt12.png")
i = 0


"""_____TUTOR___"""
tu1 = pygame.image.load("pic/tu4.png")
tu2 = pygame.image.load("pic/tu5.png")
tu3 = pygame.image.load("pic/tu6.png")
tu4 = pygame.image.load("pic/tu7.png")
tu5 = pygame.image.load("pic/tu8.png")



