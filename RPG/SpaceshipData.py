import pygame
import random
from spaceship import Spaceship
from baddie import Baddie
from player import *
from enemy import Enemy
import filestuff as FS
import drawstuff as Draw


class SpaceshipData:

    def __init__(self,width,height,frame_rate):
        self.font = pygame.font.SysFont("Times New Roman",36)
        self.font3 = pygame.font.SysFont("Times New Roman",26)
        self.font2 = pygame.font.SysFont("Courier New",20)
        self.frame_rate = frame_rate
        self.text_color = (255,0,0)
        self.width  = width
        self.height = height
        self.upper_limit = self.width/3
        self.spaceship_width = 20
        self.spaceship_height = 20
        self.spaceship = Spaceship(self.spaceship_width,self.spaceship_height,(self.width / 2),(self.height / 2) - 10, (255,255,255))
        self.player_width = 50
        self.player_height = 50
        self.player = Player(self.player_width,self.player_height,(self.width / 8)+50,(self.height / 2) + 50, (255,255,255))
        self.player2 = Player2(self.player_width,self.player_height,(self.width / 2)-150,(self.height / 2) + 50, (155,155,255))
        self.player3 = Player3(self.player_width,self.player_height,(self.width / 2)+50,(self.height / 2) + 50, (155,255,155))
        self.spaceship_speed = 5
        self.bullets = []
        self.bullet_width = 10
        self.bullet_height = 5
        self.bullet_color = (255,255,255)
        self.baddies = []
        self.baddie_width = 20
        self.baddie_height = 20
        self.baddie_color = (255,0,0)
        self.battle = 0
        self.text = 0
        
        self.players = [self.player, self.player2, self.player3]

        self.enemy1= None
        self.enemy2 = None
        self.enemy3 = None
        self.enemies = []
        self.alive_enemies = []
        self.enemy_width = 50
        self.enemy_height = 50
        self.enemy_color = (255,0,0)
        self.eslots = []

        self.number = 10
        self.itemAt =1
        self.turn =1
        self.member_turn = 1
        self.items = self.player.items

        self.fleeN = 0

        self.badMemTurn = 0
        self.currentBad = None
        self.selectedPlayerAt = 1
        self.selectedBad = self.enemy1
        self.selectedBadAt = 1
        self.badnum = 0
        self.enemyLoaded = 0

        self.spell = FS.loadSpell1()
        self.specials = self.spell[0]
        self.specialcost = self.spell[1]
        self.specialAt = 1

        self.xOn = 0
        self.x2On = 0
        self.yOn = 0
        self.y2On = 0
        self.aOn = 0
        self.a2On = 0
        self.bOn = 0


        FS.load(self.player)
        FS.load(self.player2)
        FS.load(self.player3)
        self.currentPlayer = self.player3
        return



    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):

        if pygame.K_p in newkeys:
            FS.save(self.spaceship)
            print "Saving..."
        if pygame.K_a in keys:
            self.spaceship.moveLeft(self.spaceship_speed)
        if pygame.K_d in keys:
            self.spaceship.moveRight(self.spaceship_speed)
        if pygame.K_w in keys:
            self.spaceship.moveUp(self.spaceship_speed)
        if pygame.K_s in keys:
            self.spaceship.moveDown(self.spaceship_speed)
        if pygame.K_y in newkeys:
            self.battle = -1
            self.battleEvolve(keys, newkeys, buttons, newbuttons, mouse_position)
        if pygame.K_1 in newkeys:
            self.addBaddie()

        #if pygame.K_SPACE in newkeys:
         #   self.bullets.append(self.spaceship.fire(self.bullet_width,self.bullet_height,self.bullet_color))


        for bullet in self.bullets:
            bullet.moveBullet()
            bullet.checkBackWall(self.width)
                
        for baddie in self.baddies:
            baddie.tick(0,0,self.height)



        for bullet in self.bullets:
            if not bullet.alive:
                continue
            for baddie in self.baddies:
                if not baddie.alive:
                    continue
                x,y,w,h = baddie.getDimensions()
                bullet.checkHitBaddie(x,y,w,h)
                if bullet.getHit():
                    bullet.setAlive(False)
                    baddie.setAlive(False)
                    bullet.hit = False
        for baddie in self.baddies:
            if not baddie.alive:
                continue
            x,y,w,h = baddie.getDimensions()
            self.spaceship.checkHit(x,y,w,h)

            if self.spaceship.hit == True:
                self.spaceship.hit = False
                self.battle = -1
                baddie.alive = False

        live_bullets = []
        live_baddies = []
        for bullet in self.bullets:
            if bullet.alive:
                live_bullets.append(bullet)
        for baddie in self.baddies:
            if baddie.alive:
                live_baddies.append(baddie)
      
        self.bullets = live_bullets
        self.baddies = live_baddies
            
        return

    def battleEvolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        if pygame.K_KP_ENTER in keys:
            self.battle = 0

        if(self.member_turn >= 4):
            self.member_turn = 1
            if(self.fleeN >=2):
                self.battle = 0
            self.turn = 0

        if(self.enemyLoaded == 0):
            self.enemies = [None, None, None]
            self.enemy1 = Enemy( self.enemy_width, self.enemy_height, self.width-300, 200, (255,0,0),"redslime.txt" )
            self.enemy2 = Enemy( self.enemy_width, self.enemy_height, self.width-200, 200, (0,255,0),"greenslime.txt" )
            self.enemy3 = Enemy( self.enemy_width, self.enemy_height, self.width-100, 200, (0,0,255),"blueslime.txt" )
            self.enemies[0]=self.enemy1
            self.enemies[1]=self.enemy2
            self.enemies[2]=self.enemy3
            self.eslots= [self.enemy1, self.enemy2, self.enemy3]
            self.enemyLoaded = 1




        if(self.eslots == [None, None, None]):
            self.battle = 0
            self.enemyLoaded = 0
            print "Win!"

        if (self.eslots[0] != None):
            if(self.eslots[0].health <=0):
                self.eslots[0] = None
                self.badnum -= 1
                if (self.eslots[2] != None):
                    self.selectedBadAt -=1
                else:
                    self.selectedBadAt += 1
        if (self.eslots[1] != None):
            if(self.eslots[1].health <=0):
                self.eslots[1] = None
                self.badnum -= 1
                if (self.eslots[0] != None):
                    self.selectedBadAt -=1
                else:
                    self.selectedBadAt += 1
        if (self.eslots[2] != None):
            if(self.eslots[2].health <=0):
                self.eslots[2] = None
                self.badnum -= 1
                if(self.eslots[1]!= None):
                    self.selectedBadAt -=1
                else:
                    self.selectedBadAt += 1

        print self.selectedBadAt

        if(self.turn == 1):
            if(self.member_turn == 1 or self.member_turn == 2 or self.member_turn == 3):
                if(self.member_turn == 1):
                    self.currentPlayer = self.player
                elif(self.member_turn == 2):
                    self.currentPlayer = self.player2
                elif(self.member_turn == 3):
                    self.currentPlayer = self.player3


                if pygame.K_i in newkeys:
                    if(self.xOn == 0):
                        self.xOn =1
                    else:
                        self.currentPlayer.useItem(self.items[self.itemAt-1])
                        self.member_turn +=1
                        self.xOn = 0

                    if(self.yOn == 1):
                        self.yOn = 0
                    if(self.y2On== 1):
                        self.y2On = 0

                    if(self.aOn == 1):
                        self.aOn = 0
                    if(self.a2On == 1):
                        self.a2On = 0

                    if(self.bOn == 1):
                        self.bOn = 0

                n = 0
                while(n == 0):
                    self.badnum = 0
                    if (self.eslots[0] != None):
                        self.badnum += 1
                    if (self.eslots[1] != None):
                       self.badnum += 1
                    if (self.eslots[2] != None):
                        self.badnum += 1

                    n = 1

                if(self.selectedBadAt <= 0):
                    a = 0
                    for _ in self.eslots:
                        if(self.eslots[a] != None):
                            self.selectedBadAt =  self.badnum
                        a+= 1
                if(self.selectedBadAt > self.badnum):
                    f = 0
                    for _ in self.eslots:
                        if(self.eslots[f] != None):
                            self.selectedBadAt = f- self.badnum +2
                        f+= 1

                if(self.selectedBadAt == 1):
                    if (self.eslots[0] != None):
                        self.selectedBad = self.enemy1
                    else:
                        self.selectedBadAt =2
                elif(self.selectedBadAt == 2):
                    if (self.eslots[1] != None):
                        self.selectedBad = self.enemy2
                    else:
                        self.selectedBadAt =3
                elif(self.selectedBadAt == 3):
                    if (self.eslots[2] != None):
                        self.selectedBad = self.enemy3
                    else:
                        self.selectedBadAt =1

                if(self.y2On == 1 or self.a2On == 1):
                        if pygame.K_a in newkeys:
                            self.selectedBadAt -= 1
                        if pygame.K_d in newkeys:
                            self.selectedBadAt += 1
                if pygame.K_j in newkeys:
                    if(self.y2On == 1):
                        self.selectedBad.health -= int(self.specialcost[self.specialAt-1])
                        self.player.mana -= int(self.specialcost[self.specialAt-1])
                        self.member_turn +=1
                        self.y2On = 0
                        self.yOn = 0
                    else:
                        if(self.yOn == 0):
                            self.yOn =1
                        else:
                            if(self.player.mana >= int(self.specialcost[self.specialAt-1])):
                                self.y2On = 1
                                self.yOn = 0
                            else:
                                print "Not enough mana"


                    if(self.xOn == 1):
                        self.xOn = 0

                    if(self.aOn == 1):
                        self.aOn = 0

                    if(self.bOn == 1):
                        self.bOn = 0

                if pygame.K_l in newkeys:
                    if(self.a2On == 1):
                        self.selectedBad.health -= int(2)
                        self.member_turn +=1
                        self.a2On = 0
                        self.aOn = 0
                    else:
                        if(self.aOn == 0):
                            self.aOn =1
                        else:
                            if(self.player.mana >= 0):
                                self.a2On = 1
                                self.aOn = 0
                            else:
                                print "Not enough mana"

                    if(self.xOn == 1):
                        self.xOn = 0

                    if(self.yOn == 1):
                        self.yOn = 0

                    if(self.bOn == 1):
                        self.bOn = 0

                if pygame.K_k in newkeys:
                    if(self.bOn == 0):
                        self.bOn =1
                    else:
                        self.bOn = 0
                        self.member_turn += 1
                        self.fleeN += 1


                    if(self.xOn == 1):
                        self.xOn = 0

                    if(self.yOn == 1):
                        self.yOn = 0


                    if(self.aOn == 1):
                        self.aOn = 0

                if(self.xOn==1):
                    if pygame.K_s in newkeys:
                        self.itemAt += 1
                    if pygame.K_w in newkeys:
                        self.itemAt -= 1

                if(self.yOn==1):
                    if pygame.K_s in newkeys:
                        self.specialAt += 1
                    if pygame.K_w in newkeys:
                        self.specialAt -= 1
        else:
            if(self.selectedPlayerAt == 1):
                if (self.players[0] != None):
                    self.selectedPlayer = self.player
                else:
                    self.selectedPlayerAt =2
            elif(self.selectedPlayerAt == 2):
                if (self.players[1] != None):
                    self.selectedPlayer = self.player2
                else:
                    self.selectedPlayerAt =3
            elif(self.selectedPlayerAt == 3):
                if (self.players[2] != None):
                    self.selectedPlayer = self.player3
                else:
                    self.selectedPlayerAt =1
            
            
            
            self.currentBad = self.enemy1
            if( self.eslots[0] != None):
                self.selectedPlayer = self.players[random.randint(-1,2)]
                self.selectedPlayer.health -= 3
            if( self.eslots[0] != None):
                self.selectedPlayer = self.players[random.randint(-1,2)]
                self.selectedPlayer.health -= 3
            if( self.eslots[0] != None):
                self.selectedPlayer = self.players[random.randint(-1,2)]
                self.selectedPlayer.health -= 3
            self.turn = 1

        n = len(self.specials)
        if (self.specialAt > n):
            self.specialAt = 1
        if(self.specialAt <=0):
            self.specialAt = n

        n = len(self.items)
        if (self.itemAt > n):
            self.itemAt = 1
        if(self.itemAt <=0):
            self.itemAt = n

        if pygame.K_t in newkeys:
            self.text = 1
        if pygame.K_r in newkeys:
            self.text = 0


        live_enemies = []
        for e in self.enemies:
            if (e != None):
                if e.alive:
                    live_enemies.append(e)

        self.enemies = live_enemies

        return

    def addBaddie(self):
        new_baddie = Baddie( self.baddie_width, self.baddie_height, self.width, random.randint(0,(self.height-self.baddie_height)), self.baddie_color )
        self.baddies.append( new_baddie )
        return


    def draw(self,surface):
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill((0,0,0),rect )
        self.spaceship.draw(surface)
        for bullet in self.bullets:
            bullet.draw(surface)
        for baddie in self.baddies:
            baddie.draw(surface)
        return

    def battleDraw(self,surface):
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill((175,175,50),rect )

        self.player.draw(surface)
        self.drawTextLeft(surface, str(self.player.health),(0,0,0),10,300,self.font3)
        self.player2.draw(surface)
        self.drawTextLeft(surface, str(self.player2.health),(0,0,0),10,250,self.font3)
        self.player3.draw(surface)
        self.drawTextLeft(surface, str(self.player3.health),(0,0,0),10,200,self.font3)
        self.currentPlayer.draw(surface)
        for e in self.eslots:

             if (e == "None" or e == None):
                continue
             else:
                e.draw(surface)

        if(self.turn == 1):
            if(self.member_turn == 1 or self.member_turn == 2 or self.member_turn == 3):
                if (self.y2On == 1 or self.a2On == 1):
                    if ( self.selectedBad != None):
                        Draw.drawRect(surface,self.selectedBad.x,self.selectedBad.y+55, 50,10,(0,150,155))
                        Draw.drawBREct(surface,100, 50,150, 50)
                        self.drawTextLeft(surface, self.selectedBad.name,(0,0,0),105,95,self.font3)


                if(self.xOn == 1):
                    Draw.drawRect(surface,self.currentPlayer.x-60,self.currentPlayer.y-60, 170,50,(255,255,255))
                    Draw.drawRect(surface,self.currentPlayer.x-60,self.currentPlayer.y-60, 170,50,(0,0,0,),5)
                    self.drawTextRight(surface, "Item",(0,0,0),self.currentPlayer.x+ 30,self.currentPlayer.y-20,self.font)

                    Draw.drawRect(surface,450,330,500,250,(255,255,255))
                    Draw.drawRect(surface,450,330,500,250,(0,0,0),5)
                    n = 0
                    for a in self.items:
                        self.drawTextLeft(surface, a,(0,0,0),460,380+35*n,self.font3)
                        n+=1
                    n=0

                    if(self.items):
                        Draw.drawRect(surface,455,315+35*self.itemAt,245,30,(0,0,0),5)
                else:
                    # X square
                    Draw.drawRect(surface, self.currentPlayer.x,self.currentPlayer.y-60, 50,50,(255,255,255))
                    Draw.drawRect(surface,self.currentPlayer.x,self.currentPlayer.y-60, 50,50,(0,0,0),5)

                    self.drawTextRight(surface, "X",(0,0,0),self.currentPlayer.x+ 30,self.currentPlayer.y-20,self.font)

                if(self.yOn == 1):
                    m = 50
                    if(self.currentPlayer == self.player3):
                        m = 150
                    Draw.drawRect(surface,self.currentPlayer.x-130-m,self.currentPlayer.y,170,50,(255,255,255))
                    Draw.drawRect(surface,self.currentPlayer.x-130-m,self.currentPlayer.y,170,50,(0,0,0),5)
                    self.drawTextRight(surface, "Special",(0,0,0),self.currentPlayer.x-m,self.currentPlayer.y+50,self.font)


                    Draw.drawBREct(surface,480,300,300,50)

                    Draw.drawRect(surface,450,330,500,250,(255,255,255))
                    Draw.drawRect(surface,450,330,500,250,(0,0,0),5)

                    n = 0
                    for a in self.specials:
                        if(self.player.mana >= int(self.specialcost[self.specialAt-1])):
                            color = (0,0,255)
                        else:
                            color =(0,0,0)
                        self.drawTextLeft(surface, a,color,460,380+35*n,self.font3)
                        n+=1
                    n=0
                    for a in self.specialcost:
                        self.drawTextRight(surface, a,(0,0,0),900,380+35*n,self.font3)
                        n+=1
                    n=0

                    if(self.specials):
                        Draw.drawRect(surface,455,315+35*self.specialAt,450,30,(0,0,0),5)
                    self.drawTextLeft(surface, "MP "+str(self.player.mana),(0,0,0),485,330,self.font2)
                else:
                    #Y square
                    Draw.drawRect(surface,self.currentPlayer.x-60,self.currentPlayer.y, 50,50,(255,255,255))
                    Draw.drawRect(surface,self.currentPlayer.x-60,self.currentPlayer.y, 50,50,(0,0,0,),5)
                    #Draw.drawY(surface, (0,0,0), (600, 200), (650, 200),(625,225),(625,250), 5)
                    self.drawTextRight(surface, "Y",(0,0,0),self.currentPlayer.x-20,self.currentPlayer.y+50,self.font)

                if(self.aOn == 1):
                    Draw.drawRect(surface,self.currentPlayer.x+60,self.currentPlayer.y,150,50,(255,255,255))
                    Draw.drawRect(surface,self.currentPlayer.x+60,self.currentPlayer.y,150,50,(0,0,0),5)
                    self.drawTextRight(surface, "Attack",(0,0,0),self.currentPlayer.x+200,self.currentPlayer.y+50,self.font)
                else:
                    if(self.yOn == 1):
                        if(self.currentPlayer == self.player3):
                            return
                            #A square
                    Draw.drawRect(surface,self.currentPlayer.x+60,self.currentPlayer.y, 50,50,(255,255,255))
                    Draw.drawRect(surface,self.currentPlayer.x+60,self.currentPlayer.y, 50,50,(0,0,0,),5)
                    self.drawTextRight(surface, "A",(0,0,0),self.currentPlayer.x+100,self.currentPlayer.y+50,self.font)


                if(self.bOn == 1):
                    Draw.drawRect(surface,self.currentPlayer.x-60,self.currentPlayer.y+60,170,50,(255,255,255))
                    Draw.drawRect(surface,self.currentPlayer.x-60,self.currentPlayer.y+60,170,50,(0,0,0),5)
                    self.drawTextRight(surface, "Run Away",(0,0,0),self.currentPlayer.x+ 90,self.currentPlayer.y+110,self.font)
                else:

                    if(self.yOn == 1):
                        if(self.currentPlayer == self.player3):
                            return
                    #B square
                    Draw.drawRect(surface,self.currentPlayer.x,self.currentPlayer.y+60, 50,50,(255,255,255))
                    Draw.drawRect(surface,self.currentPlayer.x,self.currentPlayer.y+60, 50,50,(0,0,0,),5)
                    self.drawTextRight(surface, "B",(0,0,0),self.currentPlayer.x+35,self.currentPlayer.y+110,self.font)

        if (self.text == 1):
            Draw.drawRect(surface,self.player.x-30,self.player.y-15, 100,150,(0,0,0))
            Draw.drawRect(surface,self.player.x-25,self.player.y-5, 90,130,(255,255,255,))

        return
    
    def drawTextLeft(self, surface, text, color, x, y,font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomleft = (x, y)
        surface.blit(textobj, textrect)
        return

    def drawTextRight(self, surface, text, color, x, y,font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomright = (x, y)
        surface.blit(textobj, textrect)
        return


