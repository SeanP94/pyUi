import pygame as pg
import random
import pygameglobals as g
import math
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
        self.ballRect.top = random.randrange(self.MAX_Y)
        self.ballRect.left = random.randrange(self.MAX_X)

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
    def __init__(self, cpath, ballSpeed=2):    
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
        self.ballRect.top = random.randrange(self.MAX_Y)
        self.ballRect.left = random.randrange(self.MAX_X)

    def dragBall(self, posTuple):
        '''
        We want to start moving the ball towards this location as we drag it.
        Thats the goal of this class

        Since there is the issue that getting the 0's just right for the area.
        We want to make sure the value is within a radius of 3
        '''

        moveList = []
        r = 3
        # Iterate over both tuples.

        for pos, ball in zip(posTuple, self.ballRect.center):
            if (ball - pos) < r and (ball - pos) > -r:
                i = 0
            else:
                i = 1 if (ball - pos) < 0 else -1
            moveList.append(i)
        print(moveList)


        # Normalize logic : Move this out later
        def normalize(moveList):
            if 0 not in moveList: 
                mag = abs(math.sqrt(moveList[0] ** 2 + moveList[1] ** 2))        
                moveList[0] = (moveList[0] * (1 / mag))
                moveList[1] = (moveList[1] * (1 / mag))#/= mag
        normalize(moveList)
        
        moveList[0] *= self.speed
        moveList[1] *= self.speed
        print(moveList)
        
        print(moveList) 
        self.ballRect.left += moveList[0]# * self.speed
        self.ballRect.top += moveList[1]# * self.speed

    def updateBall(self, event : pg.event.Event):
        """
        Takes in an event type and if the ball collides with the
        mouse, move it to a random location
        """
        print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            self.dragBall(pg.mouse.get_pos())
        # if event.type == pg.MOUSEBUTTONUP:
        #     self.dragBall(event.pos, False)
        
        self.dragBall(pg.mouse.get_pos())

    def drawBall(self, surface : pg.surface.Surface):
        surface.blit(self.ballImage, self.ballRect)

