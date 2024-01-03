import pygame, sys

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.direction = pygame.Vector2(0, 1)
        self.grow_size = pygame.Vector2(10, 10)
        self.length = 10

    def update(self, screen):
        self.rect.x += self.direction.x
        self.rect.y += self.direction.y
        
        # self.image.set_height(self.grow_size.y) 
        # self.image.set_width(self.grow_size.x)
        # self.image = nueva_superficie;
        if self.rect.x < 0 or self.rect.x > screen.get_width() or self.rect.y < 0 or self.rect.y > screen.get_height():
            pygame.quit()
            sys.exit()

    def move(self):
        # Control player2
        if (pygame.key.get_pressed()[pygame.K_UP]): 
            self.direction = pygame.Vector2(0, -1)
            self.position_y()
        if (pygame.key.get_pressed()[pygame.K_DOWN]): 
            self.direction = pygame.Vector2(0, 1)
            self.position_y()
        if (pygame.key.get_pressed()[pygame.K_RIGHT]): 
            self.direction = pygame.Vector2(1, 0)
            self.position_x()
        if (pygame.key.get_pressed()[pygame.K_LEFT]): 
            self.direction = pygame.Vector2(-1, 0)
            self.position_x()

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