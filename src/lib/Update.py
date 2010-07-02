'''
Created on Jul 1, 2010

@author: andrew
'''
import pygame
from lib import *
from pygame.locals import *


class Update:
    
    def __init__(self):
        self
        self.player = Game.player
        self.charAccel = 0
        self.charDirection = 0

    def playerUpdate(self,x, y, state, direction, moving):        
        #Game.window.blit(self.x,self.y)
        
        #Defines Acceleration
        if moving == True:
            self.charAccel += 1
        elif moving == False and self.charAccel != 0:
            self.charAccel -= 1
        if direction == -1:
            pygame.transform.flip(self.player,1,0)
            
    def displayUpdate(self):
        pass
        #Environment.drawBackground()
        #Environment.drawPlayer()