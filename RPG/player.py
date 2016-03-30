import pygame
import filestuff as FS
from bullet import Bullet

class Player():

    def __init__(self,width,height,x,y,color):
        self.rect = pygame.Rect(x, y, width, height)
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.color  = color
        self.health = 0
        self.mana = 0
        self.exp = 0
        self.weapon = "none"
        self.armor = "none"
        self.strength = 0
        self.agility = 0
        self.magic = 0
        self.gold = 0
        self.name = "Player"
        self.items = []
        return

    def loadPlayer(self):
        infoArray = FS.readFile("player.txt")
        self.name = str(infoArray[1])
        self.health = int(infoArray[3])
        self.mana = int(infoArray[5])
        self.exp= int(infoArray[7])
        self.weapon = infoArray[9]
        self.armor = infoArray[11]
        self.strength = int(infoArray[13])
        self.agility = int(infoArray[15])
        self.magic = int(infoArray[17])

        self.loadInv()

    def savePlayer(self):
        FS.rewrite("player.txt","Name "+str(self.name)+"Health " +str(self.health) + " Mana " + str(self.mana) + " EXP " +
                   str(self.exp) + " Weapon " + str(self.weapon) + " Armor " + str(self.armor) +
                   " Strength " + str(self.strength) + " Agility " + str(self.agility) + " Magic " + str(self.magic) + " endLine \nend")
        self.saveInv()
        return

    def loadInv(self):
        infoArray = FS.readFile("inventory.txt")
        self.gold = int(infoArray[1])
        n = 0
        for a in infoArray :
            if(n > 2):
                self.items.append(a)
            n += 1
        return

    def saveInv(self):
        FS.rewrite("inventory.txt","Gold " +str(self.gold) + "Items ")
        for _ in self.items:
            FS.append("inventory.txt",self.items[_])
        FS.append("inventory.txt"," endLine \nend")
        return



    def useItem(self, item):
        self.items.remove(item)
        print "Item was used"
        return

    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return

class Player2():

    def __init__(self,width,height,x,y,color):
        self.rect = pygame.Rect(x, y, width, height)
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.color  = color
        self.health = 0
        self.exp = 0
        self.weapon = "none"
        self.armor = "none"
        self.name = "player2"
        self.strength = 0
        self.agility = 0
        self.magic = 0
        self.items = []
        return

    def loadPlayer(self):
        infoArray = FS.readFile("player2.txt")
        self.name = str(infoArray[1])
        self.health = int(infoArray[3])
        self.exp= int(infoArray[5])
        self.weapon = infoArray[7]
        self.armor = infoArray[9]
        self.strength = int(infoArray[11])
        self.agility = int(infoArray[13])
        self.magic = int(infoArray[15])

    def savePlayer(self):
        FS.rewrite("player2.txt","Name "+str(self.name)+"Health " +str(self.health)  + " EXP " +
                   str(self.exp) + " Weapon " + str(self.weapon) + " Armor " + str(self.armor) +
                   " Strength " + str(self.strength) + " Agility " + str(self.agility) + " Magic " + str(self.magic) + " endLine \nend")
        return

    def useItem(self, item):
        self.items.remove(item)
        print "Item was used"
        return

    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return

class Player3():

    def __init__(self,width,height,x,y,color):
        self.rect = pygame.Rect(x, y, width, height)
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.color  = color
        self.health = 0
        self.exp = 0
        self.weapon = "none"
        self.armor = "none"
        self.name = "player3"
        self.strength = 0
        self.agility = 0
        self.magic = 0
        self.items = []
        return

    def loadPlayer(self):
        infoArray = FS.readFile("player3.txt")
        self.name = str(infoArray[1])
        self.health = int(infoArray[3])
        self.exp= int(infoArray[5])
        self.weapon = infoArray[7]
        self.armor = infoArray[9]
        self.strength = int(infoArray[11])
        self.agility = int(infoArray[13])
        self.magic = int(infoArray[15])

    def savePlayer(self):
        FS.rewrite("player3.txt","Name "+str(self.name)+"Health " +str(self.health) + " EXP " +str(self.exp) + " Weapon " + str(self.weapon) + " Armor " + str(self.armor) +
                   " Strength " + str(self.strength) + " Agility " + str(self.agility) + " Magic " + str(self.magic) + " endLine \nend")
        return

    def useItem(self, item):
        self.items.remove(item)
        print "Item was used"
        return

    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return

