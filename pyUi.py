import pygame as pg
import sys 
from pathlib import Path

cpath = Path(__file__).resolve().parent
sys.path.insert(1, str(cpath/'src'))
sys.path.insert(1, str(cpath/'logger'))


import pygameglobals as g
import colors as cls
import uiobjs as ui

from ballGame import BallDrag as BallGame # Simple UI test games Im using to find reusable code to build
from errLog import logError # Logs errors passed in from error handler.



pg.init()
# Get the screen Surface and the clock to limit fps.
window = pg.display.set_mode((g.SCREEN_WIDTH, g.SCREEN_HEIGHT))
clock = pg.time.Clock()
ball = BallGame(cpath=cpath)

# TEMP
button = ui.Button(fnUp=cpath/"images/b1.png", fnDown=cpath/"images/b2.png", x=300, y=300)
mainfont = cpath/'objs/VT323-Regular.ttf'
t =  ui.SimpleText(window, (0, 100), f" :: Shin Megami Tensei is a cool game :: ", cls.BLACK, mainfont)

def eventHandler():
    global fonts, z
    '''Placeholder for handling events (Input)'''
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

        # Pass event over to other portions of engine.
        ball.updateBall(event)
        button.handleEvents(event)

def update():
    '''Placeholder for passing to process logic'''
    ball.dragBall(pg.mouse.get_pos())


def draw():
    '''Placeholder for passing process to draw to screen'''
    # LIGHT_GRAY is essentially our "clear" the screen color.
    window.fill(cls.LIGHT_GRAY)
    ball.drawBall(window)
    button.draw(window)
    t.draw()
def gameLoop():
    '''
    Main Game looop for this test application.
    '''
    while g.RUN_FLAG:
        # Handle input
        eventHandler()
        update()
        draw()
        pg.display.update() # Update the window.s
        clock.tick(g.FPS) # Cap 60FPS


# This file wont always be main. But it will run this as a test.
if __name__ == '__main__':
    gameLoop()