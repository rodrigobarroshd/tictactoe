import imp
from turtle import width
import pygame as pg, sys    
from pygame.locals import *
import time


# Initialize global variables

XO = 'x'
Winner = None
Draw = False
width = 400
height = 400
white = (255, 255, 255)
line_color = (10, 10,10)

# 3x3 Board
TTT = [ [None]*3, [None] *3, [None] *3]


# Initializing pygame window
pg.init()

fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100), 0, 32)

pg.display.set_caption("Tic Tac Toe")


# loading the images

opening = pg.image.load('tic tac opening.png')
x_img = pg.image.load('X.png')
o_img = pg.image.load('O.png')

#resizing images
x_img = pg.transform.scale(x_img, (80,80))
o_img = pg.transform.scale(o_img, (80,80))
opening = pg.transform.scale(opening, (width, height+100))