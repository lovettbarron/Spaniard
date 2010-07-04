'''
Created on Jul 1, 2010

@author: andrew
'''
import pygame,sys

k_up = k_down = k_right = k_left = 0 #Key construct

class Control:

    def __init__(self):
        self
        
        
    def keyEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
            

        
#        for event in pygame.event.get():
#            if not hasattr(event, 'key'): continue
#            down = event.type == pygame.KEYDOWN    # key down or up?
#            if event.key == pygame.K_RIGHT: 
#                k_right = 
#            elif event.key == pygame.K_LEFT: 
#                k_left = down * 5
#            elif event.key == pygame.K_UP: 
#                k_up = down * 2
#            elif event.key == pygame.K_DOWN: 
#                k_down = down * 2
#            elif event.key == pygame.K_ESCAPE: 
#                sys.exit(0)    # quit the game
        
    def mouseEvent(self):
        pass
    
    