import pygame

def drawRect(surface, x, y,width, height, color=(255,255,255),lwidth=0):
       rect = pygame.Rect(x, y, width, height )
       pygame.draw.rect(surface, color, rect,lwidth)
       return

def drawBREct(surface, x, y,width, height, color=(255,255,255),color2=(0,0,0),lwidth1=0,lwidth2=5):
        rect = pygame.Rect(x, y, width, height )
        pygame.draw.rect(surface, color, rect,lwidth1)
        pygame.draw.rect(surface, color2, rect,lwidth2)
        return

def drawLine(surface, color, start_pos, end_pos, width=1):
       pygame.draw.line(surface, color, start_pos, end_pos, width)
       return

def drawX(surface, color, topLeft, bottomRight, width=1):
       bottomLeft = (bottomRight[0], topLeft[1])
       topRight = (topLeft[0]),(bottomRight[1])
       drawLine(surface, color, topLeft, bottomRight, width)
       drawLine(surface, color, bottomLeft, topRight, width)
       return

def drawY(surface, color, topLeft, topRight, center,centerBottom, width=1):
    drawLine(surface,color,topLeft,center, width)
    drawLine(surface, color, center,topRight, width)
    drawLine(surface,color,center, centerBottom, width)

def drawA(surface, color,centerTop,centerLeft,centerRight,centerBRight,centerBLeft,width):
    drawLine(surface,color, centerTop,centerBRight, width)
    drawLine(surface, color, centerTop, centerBLeft, width)
    drawLine(surface,color,centerLeft,centerRight, width)


def fade():
    tick = 0
    tick+=1
    while(tick >= 1):
        tick += 1

        if(tick >= 1200000):
            tick = 0
    return 1