import pygame as pg
import sys, os 
from pathlib import Path

cpath = Path(__file__).resolve().parent
sys.path.insert(1, str(cpath/'src'))
sys.path.insert(1, str(cpath/'logger'))

import colors as cls
from errLog import logError


# Temp Globals
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

pg.init()
 
# # # # # X
# Temp    #
# Globals # 
# # # # # #

ballImage = pg.image.load(cpath / 'images/ball.png')


# # # # # X


# Get the screen Surface and the clock to limit fps.
window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()
RUN_FLAG = True

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

def update():
    '''Placeholder for now, does nothing'''
    pass


def draw():
    # LIGHT_GRAY is essentially our "clear" the screen color.
    window.fill(cls.LIGHT_GRAY)
    window.blit(ballImage, (0,0))


def gameLoop():
    '''
    Main Game looop for this test application.
    '''
    while RUN_FLAG:
        # Handle input
        eventHandler()
        update()
        draw()

        pg.display.update() # Update the window.
        clock.tick(60) # Cap 60FPS


# This file wont always be main. But it will run this as a test.
if __name__ == '__main__':
    gameLoop()