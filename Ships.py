'''
Ship Classes
'''
import pygame
black = 0,0,0
class Ships(pygame.sprite.Sprite):
    '''
    Ship Class
    '''
    def __init__(self,width,height,screen):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        
        pygame.draw.rect(self.image,black, [0, 0, width, height])
        self.rect = self.image.get_rect()
