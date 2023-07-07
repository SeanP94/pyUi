import pygame as pg
import random
import math
import pygameglobals as g

'''
Space to add tools that I develop for 2D movement.

confineBoundaries : Keeps rect inside screen 
normalize : if the moveList contains 2 nonzero values it will multiple them by .5 (Not normal Linear Algebra normalization **)
moveCenterTowardsPoint : Takes a position and moves the rect's CENTER towards the position
randomPlacement : Takes a rectangle and randomly places it in the screen
'''


def confineBoundaries(rect : pg.rect.Rect):
    '''
    Keeps objects rect within screen bounadires.
    '''
    if rect.right > g.SCREEN_WIDTH:
        rect.right = g.SCREEN_WIDTH
    elif rect.left < 0:
        rect.left = 0
    if rect.top < 0:
        rect.top = 0
    elif rect.bottom > g.SCREEN_HEIGHT:
        rect.bottom = g.SCREEN_HEIGHT

def normalize(moveList):
    '''
    Normalizes a 2D vector so that if it's moving 2 directions
    both values will be half their current amount. 
    
    IE we want it to go left, itll be at a ratio 0f 1
    but if we go left and down itll bea ratio of .5 and .5 of each
    direction
    '''
    if 0 not in moveList:         
        moveList[0] *= .5
        moveList[1] *= .5

def moveCenterTowardsPoint(position : tuple[int, int], rectObj : pg.rect.Rect, speed : int, radius=1):
    '''
    Moves rectObj towards position. Within a radius.

    Keyword arguments:
    positon -- x, y tuple usually a mouse pos.
    rectObj -- the Rectangle object we are moving the center
        of towards position
    radius -- This is to prevent object jitters once it gets close.
        it'll stop within {radius} amount of pixels. Should always
        be at least 1 since mouse location is a little silly and
        can be between pixels*
    '''
    moveList = []
    # Iterate over both tuples. To get directions.
    for pos, myObj in zip(position, rectObj.center):
        # 0 if point is within radius
        if (myObj - pos) < radius and (myObj - pos) > -radius:
            i = 0
        else: # Else if value needs to go -1 or 1
            i = 1 if (myObj - pos) < 0 else -1
        moveList.append(i) # Adds -1, 0, or 1
    # Normalize the 2D vector.
    normalize(moveList)
    # Add the need for speed.
    moveList[0] *= speed
    moveList[1] *= speed
    
    rectObj.left += math.floor(moveList[0])
    rectObj.top += math.floor(moveList[1])
    
    # Keep rect within boundaries.
    confineBoundaries(rect=rectObj)

def randomPlacement(rectObj : pg.rect.Rect, maxX : int, maxY : int):
    """
    Based on Top Left point, places this at a random point in the screen.

    ** Note, make sure you g.SCREEN_HEIGHT - rectObj_ylen and g.SCREEN_WIDTH - rectObj_Xlen
    first so it places it within screen boundaries **

    Keyword arguments:
    rectObj -- Rectangle to move randomly.
    maxX -- CLEANED x coord that MUST be within screen
    maxY -- CLEANED y coord that MUST be within screen
    """
    rectObj.left = random.randrange(maxX)
    rectObj.top = random.randrange(maxY)

