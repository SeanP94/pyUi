import pygame as pg
import sys, os 
from pathlib import Path

cpath = Path(__file__).resolve().parent
sys.path.insert(1, str(cpath/'src'))
sys.path.insert(1, str(cpath/'logger'))

import colors as cls
from errLog import logError

import random

# Temp Globals
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60 
pg.init()
 
# # # # # X
# Temp    #
# Globals # 
# # # # # #
BALLH = 100

MAX_X = SCREEN_HEIGHT - BALLH
MAX_Y = SCREEN_WIDTH - BALLH

ballx = random.randrange(MAX_X)
bally = random.randrange(MAX_Y)
ballImage = pg.image.load(cpath / 'images/ball.png')
ballRect = pg.Rect(ballx, bally, BALLH, BALLH)

def resetBall():
    global ballx, bally, ballRect
    ballx = random.randrange(MAX_X)
    bally = random.randrange(MAX_Y)
    ballRect = pg.Rect(ballx, bally, BALLH, BALLH)
    

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

        
        if event.type == pg.MOUSEBUTTONDOWN:
            if ballRect.collidepoint(event.pos):
                print(f"{event.pos} : Booped the ball")
                resetBall()
def update():
    '''Placeholder for now, does nothing'''
    pass


def draw():
    # LIGHT_GRAY is essentially our "clear" the screen color.
    window.fill(cls.LIGHT_GRAY)
    window.blit(ballImage, (ballx,bally))


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
        clock.tick(FPS) # Cap 60FPS



# This file wont always be main. But it will run this as a test.
if __name__ == '__main__':
    gameLoop()