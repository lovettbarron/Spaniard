import pygame
from pygame.locals import *
pygame.init()

#import Update
#import Environment
#import Control

#Game variables
imageDir = "../char/"
fps = 30 #Frames per second
accel = 5 #Acceleration
speed = direction = 0

pygame.init()

#pygame.display.init()

class Game:
    def __init__(self):
        self.fontPrep()
        self.window = pygame.display.set_mode((640,480),0,32) #Game window
        
        self.ground = self.window.subsurface((0, 316, 640,480-316))
        
        
        pygame.display.set_caption("A Spaniard's Sight")
        self.player = pygame.image.load(imageDir + 'play1.png').convert_alpha() #Player character
        self.trail = pygame.image.load(imageDir + 'trail.png').convert() #Trail
        self.house = pygame.image.load(imageDir + 'house1.png').convert() #house`
        self.rotar = pygame.image.load(imageDir + 'rotar.png').convert_alpha() #Rotar
        
        self.frame_timer = pygame.time.Clock()
        self.playerX = self.playerY = 0
        self.playerY = 300
        self.houseX = 300
        self.houseY = 300-256+16
        self.accel = 0
        self.rotate = 0
        
        self.keyDown = False
        self.eventCheck = False
        
        self.maskHouse = pygame.Mask
        self.maskPlayer= pygame.Mask
        
    ## MAIN LOOP, draws    
    def main(self):
        while True:
            self.frame_timer.tick(30)
            self.moveCommand()
            #Environment.drawBackground()
            #Environment.drawPlayer()
            #pygame.display.flip()
            
            if self.keyDown == 1:
                self.playerX += 1
            
            if self.keyDown == 1:
                self.accel += 1
            elif self.keyDown == 0 and self.accel > 0:
                self.accel = self.accel%2
            
            self.playerX += self.accel
            print self.accel
            
            self.window.fill((255,255,255))
            self.ground.fill((0,0,0))
            
            self.window.blit(self.house,(self.houseX,self.houseY))
            for trails in range(1,(self.playerX - self.accel - 1)):
                self.window.blit(self.trail,(trails,self.playerY))    
            self.window.blit(self.player,(self.playerX,self.playerY))
            
            self.rotateWindmill()
            self.detectWindmill()
            
            
            #self.playerX += 1
            
           # Update.updateLoop()
            pygame.display.update()
      
      
    def moveCommand(self):
            self.eventCheck = self.controlUpdate()
            
            if self.eventCheck != 1 and self.keyDown != 1:
                self.keyDown = 0
            elif self.eventCheck == -1 and self.keyDown == 1:
                self.keyDown = 0
            elif self.eventCheck == 1 and self.keyDown == 1:
                self.keyDown = 1
            else:
                self.keyDown = 1 
            
    def controlUpdate(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print "Spacebar pressed"
                    return 1
                elif event.key == pygame.K_ESCAPE:
                    print "Escape pressed"
                    pygame.quit()
                    exit()
                    return False                  
            elif event.type == KEYUP:
                if event.key == pygame.K_SPACE:
                    print "Spacebar released"
                    return -1
            else:
                return False
                
    def rotateWindmill(self):
            self.original = self.rotar.get_rect()
            self.rotate = (self.rotate + 1) % 90
            self.rotar_copy = pygame.transform.rotate(self.rotar,(self.rotate))
            self.rot_rect = self.original
            self.rot_rect.center = self.rotar_copy.get_rect().center
            print self.rot_rect.center
            self.window.blit(self.rotar_copy,(self.houseX+50-self.rot_rect.center[0],self.houseY-self.rot_rect.center[1]))
            
    def detectWindmill(self):
        print "Player:" + str(self.playerX+16) + "  Windmill:" + str(self.houseX)
        if self.playerX+16 >= self.houseX:
            print "ITS A WINDMILL"
            self.window.blit(self.type("OH MY GOD IT\'S A WINDMILL"),(self.playerX-200,self.playerY+100))
            
    def fontPrep(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('Advocut,Luxi Mono,Arial,Helvetica',14,True,False)
        
    def type(self,toSay):
        self.font_image = self.font.render(toSay,False,(255,255,255))
        return self.font_image
    
if __name__.lower() == '__main__':
    Game().main()
