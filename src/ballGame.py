import pygame as pg
import random
import pygameglobals as g
import math

### Functions that need to be exported eventually into a 2D Movement class.

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

class BallRand():
    def __init__(self, cpath):    
        self.BALLH = 100
        self.MAX_X = g.SCREEN_HEIGHT - self.BALLH
        self.MAX_Y = g.SCREEN_WIDTH - self.BALLH

        self.ballImage = pg.image.load(cpath / 'images/ball.png')
        self.ballRect = self.ballImage.get_rect()
        self.resetBall() # Set balls pos


    def resetBall(self):
        """
        Resets the ball to a random location on the screen.
        """
        randomPlacement(self.ballRect, self.MAX_X, self.MAX_Y)

    def updateBall(self, event : pg.event.Event):
        """
        Takes in an event type and if the ball collides with the
        mouse, move it to a random location
        """
        if self.ballRect.collidepoint(event.pos):
            print(f"{event.pos} : Booped the ball")
            self.resetBall()

    def drawBall(self, surface : pg.surface.Surface):
        surface.blit(self.ballImage, self.ballRect)

class BallDrag():
    def __init__(self, cpath, ballSpeed=10):    
        self.BALLH = 100
        self.speed = ballSpeed
        self.MAX_X = g.SCREEN_HEIGHT - self.BALLH
        self.MAX_Y = g.SCREEN_WIDTH - self.BALLH

        self.ballImage = pg.image.load(cpath / 'images/ball.png')
        self.ballRect = self.ballImage.get_rect()
        self.resetBall() # Set balls pos


    def resetBall(self):
        """
        Resets the ball to a random location on the screen.
        """
        randomPlacement(self.ballRect, self.MAX_X, self.MAX_Y)

    def dragBall(self, posTuple):
        '''
        We want to start moving the ball towards this location as we drag it.
        Thats the goal of this class

        Since there is the issue that getting the 0's just right for the area.
        We want to make sure the value is within a radius of 5
        
        The radius should be controlled by the size of the pixels.
        Note this for when building a real feature.

        '''
        moveCenterTowardsPoint(posTuple, self.ballRect, self.speed, radius=5)

    def updateBall(self, event : pg.event.Event):
        """
        Takes in an event type and if the ball collides with the
        mouse, move it to a random location
        """
        if event.type == pg.MOUSEBUTTONDOWN:
            self.dragBall(pg.mouse.get_pos())
        self.dragBall(pg.mouse.get_pos())

    def drawBall(self, surface : pg.surface.Surface):
        surface.blit(self.ballImage, self.ballRect)

