import pygame, sys
from src.snake import Snake
    
class SnakeActions():
    def __init__(self, snake):
        self.snake = snake
    
    def update(self, snake_segments, screen):
        # TODO
        # if self.snake.rect.x < 0 or self.snake.rect.x > screen.get_width() or self.snake.rect.y < 0 or self.snake.rect.y > screen.get_height():
        #     pygame.quit()
        #     sys.exit()

        # self.snake.rect.x += self.snake.direction.x
        # self.snake.rect.y += self.snake.direction.y
        # self.image.set_height(self.grow_size.y) 
        # self.image.set_width(self.grow_size.x)
        # Mueve la serpiente en la dirección actual
         # Mueve la serpiente en la dirección actual
        head = snake_segments[0]
        new_x = head.rect.x + self.snake.direction[0] * head.rect.width
        new_y = head.rect.y + self.snake.direction[1] * head.rect.height

        # Añade un nuevo segmento en la posición actual de la cabeza
        new_segment = Snake(new_x, new_y, head.rect.width, head.rect.height)
        snake_segments.insert(0, new_segment)

    def move(self):
        # Control player2
        if (pygame.key.get_pressed()[pygame.K_UP]): self.snake.direction = pygame.Vector2(0, -1)
        if (pygame.key.get_pressed()[pygame.K_DOWN]): self.snake.direction = pygame.Vector2(0, 1)
        if (pygame.key.get_pressed()[pygame.K_RIGHT]): self.snake.direction = pygame.Vector2(1, 0)
        if (pygame.key.get_pressed()[pygame.K_LEFT]): self.snake.direction = pygame.Vector2(-1, 0)