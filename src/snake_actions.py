import pygame, sys
from src.snake import Snake
    
class SnakeActions() :
    def __init__(self, snake):
        self.snake = snake
    
    def move(self):
        # Control player2
        if (pygame.key.get_pressed()[pygame.K_UP]): self.snake.direction = pygame.Vector2(0, -1)
        if (pygame.key.get_pressed()[pygame.K_DOWN]): self.snake.direction = pygame.Vector2(0, 1)
        if (pygame.key.get_pressed()[pygame.K_RIGHT]): self.snake.direction = pygame.Vector2(1, 0)
        if (pygame.key.get_pressed()[pygame.K_LEFT]): self.snake.direction = pygame.Vector2(-1, 0)