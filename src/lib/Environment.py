'''
Created on Jul 1, 2010

@author: andrew
'''
import pygame

class Environment:
    
    def __init__(self):
        self
        
    def drawPlayer(self):
        pass
    
    def drawBackground(self):
        Game.window.fill((125,239,19))
        
        
    def block(self,surface, height):
        pygame.draw.rect(surface, (255,255,255) (0,0,height,height))
    
    