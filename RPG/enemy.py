import pygame
import random
import filestuff as FS

class Enemy():

    def __init__(self,width,height,x,y,color,file):
        self.file = file
        self.rect = pygame.Rect(x, y, width, height)
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.new_x  = x
        self.new_y  = y
        self.speed  = 3
        self.name = file
        self.color  = color
        self.alive  = True
        self.health = 10
        self.mana = 0
        self.strength = 1
        self.agility = 1
        self.magic = 1
        return

    def loadEnemy(self,baddieFile):
        infoArray = FS.readFile(baddieFile)
        self.name = baddieFile - ".txt"
        self.health = int(infoArray[1])
        self.mana = float(infoArray[3])
        self.strength = int(infoArray[5])
        self.agility = int(infoArray[7])
        self.magic = int(infoArray[9])

    def saveEnemy(self,baddieFile):
        FS.rewrite(baddieFile,"Health " +str(self.health) + " Mana " + str(self.mana) +
                   " Strength " + str(self.strength) + " Agility " + str(self.agility) + " Magic " + str(self.magic) + " endLine \nend")
        return

    def getAlive(self):
        return self.alive

    def getDimensions(self):
        return self.x,self.y,self.width,self.height

    def setAlive(self,alive):
        self.alive = alive

    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return


