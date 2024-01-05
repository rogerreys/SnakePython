import pygame

class Food(pygame.sprite.Sprite):
    def __init__(self, x, y, config_file):
        super().__init__()
        # Obtiene las variables del archivo de configuración
        w = config_file["food"]["width"]
        h = config_file["food"]["height"]

        self.image = pygame.Surface((w, h))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y