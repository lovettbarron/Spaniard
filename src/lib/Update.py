import pygame


class Update:
    
    def __init__(self,Game):
        self.player = Game.player
        self.window = Game.window
        self.charAccel = 0
        self.charDirection = 0
        self.x = 0

    def updateLoop(self):
        if Control.keyEvent == True:
            self.x += 1
            self.window.blit( self.player (self.x,0))

#    def playerUpdate(self, x, y, state, direction, moving):        
#        Game.window.blit(self.x,self.y)
#        
#        #Defines Acceleration
#        if moving == True:
#            self.charAccel += 1
#        elif moving == False and self.charAccel != 0:
#            self.charAccel -= 1
#        if direction == -1:
#            pygame.transform.flip(self.player,1,0)
#            
    def displayUpdate(self):
        pass
        #Environment.drawBackground()
        #Environment.drawPlayer()