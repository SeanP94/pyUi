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
        self.rect.top = self.loc[1]

    def handleEvents(self, event):
        """
        The button events will basically run if somehtings been pressed.
        The button functionality works if you click on the button and release
        return True

        Else change state. 
        Also allows if you press down on the button and release off the button 
        it does not execute
        but will return True if you move the mouse back over the button.
        
        """
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
            
            if event.type == pg.MOUSEMOTION and not hasCollided:
                self.state == BStates.RELEASED # Hold onto the button press

        elif self.state == BStates.RELEASED:
            if hasCollided:
                self.state = BStates.PRESSED
            elif event == pg.MOUSEBUTTONUP:
                self.state = BStates.IDLE

        return False

    def draw(self, surface : pg.surface.Surface):
        """
        Determines which button skin to draw.
        """
        if self.state == BStates.PRESSED:
            surface.blit(self.buttonDown, self.loc)
        else:
            surface.blit(self.buttonUp, self.loc)


class SimpleText():
    
    def __init__(self, window, loc, value, textColor, font):
        pg.font.init()
        self.window = window
        self.loc = loc
        self.font = pg.font.Font(font, 30)
        self.textColor = textColor
        self.text = None # so that the call to setText below will 
                         # force the creation of the text image
        self.setValue(value) # set the initial text for drawing

    def setValue(self, newText):  
        if self.text == newText:
            return  # nothing to change
        self.text = newText  # save the new text
        self.textSurface = self.font.render(self.text, True, self.textColor)

    def draw(self):
        self.window.blit(self.textSurface, self.loc)
