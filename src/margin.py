import pygame

class Margin(pygame.sprite.Sprite):
    def __init__(self, x, y, config_file):
        super().__init__()
        # Obtiene las variables del archivo de configuración
        w = config_file["margin"]["width"]
        h = config_file["margin"]["height"]

        self.image = pygame.Surface((w, h))
        self.image.fill(list(config_file["margin"]["color"]))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y