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
    def __init__(self, cpath, ballSpeed=3):    
        self.BALLH = 100
        self.ballSpeed = 3
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

    def dragBall(self, posTuple, clicked=False):
        '''
        We want to start moving the ball towards this location as we drag it.
        Thats the goal of this class

        We want to I think Normalize the data to the Mouse button being 0,0

        '''
        if clicked:
            return
        posx, posy = posTuple
        ballx, bally = self.ballRect.center
        print(posx, posy)
        print(posx - ballx, posy - bally)
        
        print(ballx, bally)
        moveList = []
        for pos, ball in zip(posTuple, self.ballRect.center):
            i = 1 if (ball - pos) < 0 else -1
            moveList.append(i * min(self.ballSpeed, abs((ball - pos) - 1)))
            print(ball, pos, ball - pos)
        print(moveList)
        # Normalize logic
        def normalize(moveList):
            if (moveList[0] > 1 or moveList[0] < -1) and (moveList[1] > 1 or moveList[1] < -1):
                v = abs(math.sqrt(moveList[0] ** 2 + moveList[1] ** 2))        
                moveList[0] /= v
                moveList[1] /= v
            
        normalize(moveList)
        print(moveList)
        self.ballRect.left += moveList[0]
        self.ballRect.top += moveList[1]

    def updateBall(self, event : pg.event.Event):
        """
        Takes in an event type and if the ball collides with the
        mouse, move it to a random location
        """
        print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            self.dragBall(pg.mouse.get_pos(), True)
        # if event.type == pg.MOUSEBUTTONUP:
        #     self.dragBall(event.pos, False)
        
        self.dragBall(pg.mouse.get_pos())

    def drawBall(self, surface : pg.surface.Surface):
        surface.blit(self.ballImage, self.ballRect)

