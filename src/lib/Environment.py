'''
Created on Jul 1, 2010

@author: andrew
'''
import pygame
from pygame.locals import *
from lib import *

class Environment:
    
    def __init__(self):
        self
        
    def drawPlayer(self):
        Game.window.blit( Game.player (0,0))
    
    def drawBackground(self):
        Game.window.fill((125,239,19))
        
        
    def block(self,surface, height):
        pygame.draw.rect(surface, (255,255,255) (0,0,height,height))
    
    