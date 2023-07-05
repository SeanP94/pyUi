import pygame as pg
import sys, os 
from pathlib import Path

cpath = Path(__file__).resolve().parent
sys.path.insert(1, str(cpath/'src'))
sys.path.insert(1, str(cpath/'logger'))

import colors as cls
from errLog import logError

import random
import pygameglobals as g
from ballGame import BallDrag as BallGame

pg.init()
# Get the screen Surface and the clock to limit fps.
window = pg.display.set_mode((g.SCREEN_WIDTH, g.SCREEN_HEIGHT))
clock = pg.time.Clock()
ball = BallGame(cpath=cpath)


def eventHandler():
    for event in pg.event.get():
        # Hit the 'X' at the top bar.
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        
        # This only works if draw() is commented out.
        pressed = pg.key.get_pressed()
        if pressed[pg.K_r]:
            window.fill(cls.RED)
        else:
            window.fill(cls.LIGHT_GRAY)

        
        if event.type == pg.MOUSEBUTTONDOWN:
            ball.updateBall(event)
        if event.type == pg.MOUSEBUTTONUP:
            ball.updateBall(event)
def update():
    '''Placeholder for now, does nothing'''
    pass


def draw():
    # LIGHT_GRAY is essentially our "clear" the screen color.
    window.fill(cls.LIGHT_GRAY)
    ball.drawBall(window)


def gameLoop():
    '''
    Main Game looop for this test application.
    '''
    while g.RUN_FLAG:
        # Handle input
        eventHandler()
        update()
        draw()
        pg.display.update() # Update the window.
        clock.tick(g.FPS) # Cap 60FPS



# This file wont always be main. But it will run this as a test.
if __name__ == '__main__':
    gameLoop()