import pygame
from game_mouse import Game
from SpaceshipData import SpaceshipData
import drawstuff as Draw

class SpaceshipAdventure(Game):

    def __init__(self, width, height, frame_rate):
        self.newGame(width,height,frame_rate)
        return
    
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        if (self.data.battle == 1):
            self.data.battleEvolve(keys, newkeys, buttons, newbuttons, mouse_position)
        elif(self.data.battle == 0):
            self.data.evolve(keys, newkeys, buttons, newbuttons, mouse_position)
        elif(self.data.battle == -1):
            self.data.battle = Draw.fade()
        else:
            print "no data used"
        return

    def paint(self, surface):
        self.data.draw(surface)
        if (self.data.battle == 1):
            self.data.battleDraw(surface)
        return

    
    def newGame(self,width, height, frame_rate):
        self.width = width
        self.height = height
        self.frame_rate = frame_rate
        Game.__init__(self, "Spaceship Adventure", width, height, frame_rate)   
        self.data = SpaceshipData(width,height,frame_rate)
        
        return
