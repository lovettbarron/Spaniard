import pygame
from lib import *

#Game variables
imageDir = "../char/"
fps = 30 #Frames per second
accel = 5 #Acceleration
speed = direction = 0

pygame.init()
pygame.display.set_caption("A Spaniard's Sight")
window = pygame.display.set_mode((640,480),0,32) #Game window
player = pygame.image.load(imageDir + 'play1.png').convert() #Player character
pygame.display.init()

class Game:
    def __init__(self):
        self
        
    ## MAIN LOOP, draws    
    def main(self):
        
        while 1:
            #self.clock.tick(60)
            Environment.drawBackground()
            Environment.drawPlayer()
            pygame.display.flip()

            