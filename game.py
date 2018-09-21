import sys, pygame
pygame.init()

size = width, height = 1000, 500
speed = [4, 4]
black = 0, 0, 0
white = 255, 255, 255
pos = 50, 50

running = True

def main():
    global running, screen
    
    pygame.init()
    screen = pygame.display.set_mode(size)
    screen.fill(black)
    pygame.display.update()
    
    while running:
        ev = pygame.event.get()
        
        for event in ev:
            drawCircle()
            pygame.display.update()
        if event.type == pygame.QUIT:
            running = False
def getPos():
    pos = pygame.mouse.get_pos()
    return(pos)
def drawCircle():
    pos = getPos()
    pygame.draw.circle(screen, white, 20)

