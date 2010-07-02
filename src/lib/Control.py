'''
Created on Jul 1, 2010

@author: andrew
'''
import pygame,sys
from pygame.locals import *
import lib

k_up = k_down = k_right = k_left = 0 #Key construct

class Control:

    def __init__(self):
        self
        
        
    def keyEvent(self):
        for event in pygame.event.get():
            if not hasattr(event, 'key'): continue
            down = event.type == KEYDOWN    # key down or up?
            if event.key == K_RIGHT: k_right = down * 5
            elif event.key == K_LEFT: k_left = down * 5
            elif event.key == K_UP: k_up = down * 2
            elif event.key == K_DOWN: k_down = down * 2
            elif event.key == K_ESCAPE: sys.exit(0)    # quit the game
        
    def mouseEvent(self):
        pass
    
    