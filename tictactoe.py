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