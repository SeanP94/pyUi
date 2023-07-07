import pygame as pg
import pygameglobals as g
import vec2dtools as v2d

### Functions that need to be exported eventually into a 2D Movement class.


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
        v2d.randomPlacement(self.ballRect, self.MAX_X, self.MAX_Y)

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
        v2d.randomPlacement(self.ballRect, self.MAX_X, self.MAX_Y)

    def dragBall(self, posTuple):
        '''
        We want to start moving the ball towards this location as we drag it.
        Thats the goal of this class

        Since there is the issue that getting the 0's just right for the area.
        We want to make sure the value is within a radius of 5
        
        The radius should be controlled by the size of the pixels.
        Note this for when building a real feature.

        '''
        v2d.moveCenterTowardsPoint(posTuple, self.ballRect, self.speed, radius=5)

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

