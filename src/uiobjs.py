import pygame as pg
import pygameglobals as g
from enum import Enum
"""
Class for creating interactable objects/Buttons/Menus and such.

"""

class BStates(Enum):
    IDLE = 1
    PRESSED = 2
    RELEASED = 3


class Button():
    def __init__(self, fnUp : str, fnDown : str, x : int, y :int, ):
        
        
        self.loc = (x, y)
        self.buttonUp = pg.image.load(fnUp)
        self.buttonDown = pg.image.load(fnDown)
        self.state = BStates.IDLE
        self.rect = self.buttonUp.get_rect()
        self.rect.left  = self.loc[0]
        self.rect.right = self.loc[1]

    def handleEvents(self, event):
        
        # We dont want to work with it unless it's a type we utilize.
        if event.type not in (pg.MOUSEMOTION, pg.MOUSEBUTTONUP, pg.MOUSEBUTTONDOWN):
            return False
        
        # Get if the variables have collided.
        hasCollided = self.rect.collidepoint(event.pos)

        # Move to pressed.
        if (self.state == BStates.IDLE 
                and event.type == pg.MOUSEBUTTONDOWN
                and hasCollided):
            self.state = BStates.PRESSED

        elif self.state == BStates.PRESSED: 
            if event.type == pg.MOUSEBUTTONUP and hasCollided:
                self.state = BStates.IDLE
                return True # Button must execute.


        



