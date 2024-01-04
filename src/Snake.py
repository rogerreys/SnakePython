import pygame, sys

class Snake(pygame.sprite.Sprite):
    def __init__(self,  x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.direction = pygame.Vector2(0, 1)
        self.grow_size = pygame.Vector2(10, 10)
        self.length = 10


    def grow(self):
        if (pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_DOWN]):
            self.grow_size.y += self.length
        if (pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_LEFT]):
            self.grow_size.x += self.length
    
    def position_y(self):
        self.grow_size.y = self.length
        self.grow_size.x = 10
    def position_x(self):
        self.grow_size.x = self.length
        self.grow_size.y = 10