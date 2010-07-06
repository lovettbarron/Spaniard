import pygame, random
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
        self.player = pygame.image.load(imageDir + 'play2.png').convert_alpha() #Player character
        self.trail = pygame.image.load(imageDir + 'trail.png').convert() #Trail
        self.house = pygame.image.load(imageDir + 'house1.png').convert() #house`
        self.rotar = pygame.image.load(imageDir + 'rotar2.png').convert_alpha() #Rotar
        
        self.frame_timer = pygame.time.Clock()
        self.playerX = self.playerY = 0
        self.playerY = 300
        self.houseX = 300
        self.houseY = 300-256+16
        self.accel = 0
        self.rotate = 0
        self.rotarA = 0
        self.score = 0
        self.died = 0
        
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
            
            if self.playerX > 640:
                self.playerX = 0
                self.houseX = random.randint(200,500)
                self.score += 1
                self.rotarA = random.randint(0,5)
            
            if self.keyDown == 1:
                self.playerX += 1
            
            if self.keyDown == 1:
                self.accel += 1
            elif self.keyDown == 0 and self.accel == 1:
                self.accel = 0
            elif self.keyDown == 0 and self.accel > 0:
                self.accel = self.accel%2
            
            self.playerX += self.accel
            #print "Accel:" + str(self.accel)
            
            self.window.fill((255,255,255))
            self.ground.fill((0,0,0))
            
            self.window.blit(self.house,(self.houseOffset()))
            for trails in range(1,(self.playerX - self.accel)):
                self.window.blit(self.trail,(trails,self.playerY ))    
            #if self.playerX >= self.houseX and self.playerX <= self.houseX:
            self.window.blit(self.player,(self.playerOffset()))
            #else:
            #self.window.blit(self.player,(self.playerOffset()))
            
            self.rotateWindmill()
            self.maskSet()
            self.detectWindmill()
            self.detectRotar() 
            #self.typeCoord()
            self.typeScore()
            
            pygame.display.update()
      
      
    def moveCommand(self):
            self.eventCheck = self.controlUpdate()
            
            if self.eventCheck != 1 and self.keyDown != 1:
                self.keyDown = 0
            elif self.eventCheck == -1 and self.keyDown == 1:
                self.keyDown = 0
            elif self.eventCheck == -1 and self.keyDown ==0:
                self.keydown = 0
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
            self.rotate = (self.rotate + 1 + self.rotarA) % 90
            self.rotar_copy = pygame.transform.rotate(self.rotar,(self.rotate))
            self.rot_rect = self.original
            self.rot_rect.center = self.rotar_copy.get_rect().center
            #print self.rot_rect.center
            self.window.blit(self.rotar_copy,(self.windmillOffset()))
    
    def detectWindmill(self):
        #print "Player:" + str(self.playerX+16) + "  Windmill:" + str(self.houseX)
        
        if self.playerX+16 >= self.houseX:
            print "ITS A WINDMILL"
            #self.window.blit(self.type("OH MY GOD IT\'S A WINDMILL"),(self.playerX-200,self.playerY+100))

    def detectRotar(self):
        self.overlap = 0
        print "Player:" + str(self.playerY) + " Rotar:" + str(self.rotar_copy.get_rect().bottom - self.rotar_copy.get_rect().center[1])
        if self.playerY >= self.rotar_copy.get_rect().bottom - self.rotar_copy.get_rect().center[1]:
                
#            self.windmillOffsetEdge = (self.rotar_copy.get_rect().left, self.rotar_copy.get_rect().bottom - self.rotar_copy.get_rect().center[1]) 
#            print "winmill Offset edge:" + str(self.windmillOffsetEdge)
#            self.overlap = self.rotarMask.overlap_area(self.playerMask,(self.playerOffset()))
#            self.overlap = self.overlap - self.playerMask.overlap_area(self.rotarMask,(self.windmillOffsetEdge))
#            
#            print "Overlap:" + str(self.overlap) 
#            print "rotarCopy:" + str(self.houseX+50-self.rot_rect.left) + "," + str(self.houseY+20-self.rot_rect.top)
            
            #if self.overlap >= 1:
            if self.playerX >= self.houseX and self.playerX <= self.houseX+128:
                self.window.blit(self.type("WINNDDMILLLL"),(100,316))
                self.playerX = 0
                self.accel = 0
                self.died += 1
            
    def fontPrep(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('Advocut,Helvetica',14,True,False)
        
    def type(self,toSay):
        self.font_image = self.font.render(toSay,False,(255,255,255))
        return self.font_image
    
    def typeScore(self):
        self.window.blit(self.type("Giants escaped:" + str(self.score)),(0,450))
        self.window.blit(self.type("Quests foiled:" + str(self.died)),(0,464))
                                   
    def typeCoord(self):
        self.window.blit(self.type(str(self.playerX) + "," + str(self.playerY)), (0,430))
    
    def flipPixel(self,image):
        return self.image.PixelArray.replace((0,0,0),(255,255,255))
    
    def windmillOffset(self):
        return (self.houseX+50-self.rot_rect.center[0],self.houseY+20-self.rot_rect.center[1])
    
    def playerOffset(self):
        return (self.playerX, self.playerY)
    
    def houseOffset(self):
        return (self.houseX, self.houseY)
    
    def maskSet(self):
        self.playerMask = pygame.mask.from_surface(self.player,0)
        self.houseMask = pygame.mask.from_surface(self.house,0)
        self.rotarMask = pygame.mask.from_surface(self.rotar_copy,0)
        #self.rotarMask = self.rotarMask.invert()
        
        #return ({ 'player' : pygame.mask.from_surface(self.player, (127)),
         #        'rotar' : pygame.mask.from_surface(self.rotar_copy, (127)),
          #       'house' : pygame.mask.from_surface(self.house, (127))
           #     })
    
if __name__.lower() == '__main__':
    Game().main()
