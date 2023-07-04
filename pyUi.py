import pygame as pg
import sys, os 

cpath = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, cpath+'/src/')
sys.path.insert(1, cpath+'/logger/')

from errLog import logError
import colors as cls


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

pg.init()

# Get the screen Surface and the clock to limit fps.
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()
RUN_FLAG = True

while RUN_FLAG:
    
    clock.tick(60) # Cap 60FPS


'''
We intitially want to create a grid... and 
'''