import pygame, sys
import random
from src.snake import Snake;
from src.snake_actions import SnakeActions;
from src.food import Food;


class SnakeGame:
    def __init__(self):
        # Screen
        self.width = 1366
        self.height = 768
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        # 
        self.snake = Snake(0, 0, 10, 10)
        self.snake_segments = [self.snake]
        self.snake_action = SnakeActions(self.snake_segments[0])
        self.food = Food(200, 200)

        #
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.snake_segments)
        self.all_sprites.add(self.food)
    
    def run(self):
        while True:
            # Procesar los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Mover la serpiente
            self.snake_action.update(self.snake_segments, self.screen)

            self.snake_action.move()

            # Verificar colisiones
            if self.snake.rect.colliderect(self.food.rect):
                # Crear una nueva pieza de comida
                self.all_sprites.remove(self.food)
                self.food = Food(random.randint(0, self.width - 10), random.randint(0, self.height - 10))
                self.all_sprites.add(self.food)
                # La serpiente ha comido la comida
                # Aumentar el tamaño de la serpiente
                self.snake.length += 10
                self.snake.grow()
                

            # Dibujar los objetos en la pantalla
            self.screen.fill((0, 0, 0))
            self.all_sprites.draw(self.screen)
            
            # Actualizar la pantalla
            pygame.display.flip()


if __name__ == "__main__":
    game = SnakeGame()
    game.run()