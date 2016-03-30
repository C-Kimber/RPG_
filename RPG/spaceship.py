import pygame
import filestuff as FS
from bullet import Bullet

class Spaceship():

    def __init__(self,width,height,x,y,color):
        self.rect = pygame.Rect(x, y, width, height)
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.color  = color
        self.hit = False
        return

    def moveLeft(self, dx):
        self.x -= dx

    def moveRight(self, dx):
        self.x += dx

    def moveUp(self, dx):
        self.y -= dx
    def moveDown(self, dx):
        self.y += dx

    def getDimensions(self):
        return self.x,self.y,self.width,self.height

    def checkHit(self,x,y,w,h):
        if self.hitRect(x, y, w, h):
            self.hit = True

    def hitRect(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)) :
                return True
        return False

    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return

        
