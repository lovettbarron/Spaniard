import pygame


class Update:
    
    def __init__(self,Game):
        self.player = Game.player
        self.window = Game.window
        self.rotar = Game.rotar
        self.charAccel = 0
        self.charDirection = 0
        self.x = 0
            
    def rotateWindmill(self):
        self.original = self.rotar.get_rect()
        self.rotate = (self.rotate + 1) % 90
        self.rotar_copy = pygame.transform.rotate(self.rotar,(self.rotate))
        self.rot_rect = self.original
        self.rot_rect.center = self.rotar_copy.get_rect().center
        print self.rot_rect.center
        self.window.blit(self.rotar_copy,(self.houseX+50-self.rot_rect.center[0],self.houseY+20-self.rot_rect.center[1]))
        
    def detectWindmill(self):
        print "Player:" + str(self.playerX+16) + "  Windmill:" + str(self.houseX)
        if self.playerX+16 >= self.houseX:
            print "ITS A WINDMILL"
            #self.window.blit(self.type("OH MY GOD IT\'S A WINDMILL"),(self.playerX-200,self.playerY+100))

    def detectRotar(self):
        self.overlap = 0
        self.rotarMask = pygame.mask.from_threshold(self.rotar_copy, (0,0,0), (0,0,0,127))
        self.playerMask = pygame.mask.from_threshold(self.player, (0,0,0), (0,0,0,127))
        #print "setPixels:" + str(self.rotarMask.count())
        self.overlap = self.rotarMask.overlap_area(self.playerMask,(self.playerX,self.playerY))
        self.overlap = self.overlap - self.playerMask.overlap_area(self.rotarMask,(self.houseX+50-self.rot_rect.left,self.houseY+20-self.rot_rect.top))
        print "Overlap:" + str(self.overlap) 
        print "rotarCopy:" + str(self.houseX+50-self.rot_rect.left) + "," + str(self.houseY+20-self.rot_rect.top)
        if self.overlap >= 1:
            self.window.blit(self.type("WINNDDMILLLL"),(self.playerX-200,self.playerY+100))
            
    def fontPrep(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('Advocut,Luxi Mono,Arial,Helvetica',14,True,False)
        
    def type(self,toSay):
        self.font_image = self.font.render(toSay,False,(255,255,255))
        return self.font_image
            

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