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
        self.snake_action = SnakeActions(self.snake)
        self.food = Food(200, 200)

        #
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.snake)
        self.all_sprites.add(self.food)

        self.length = 10
        self.clock_speek = 10
    
    def run(self):
        while True:
            # Procesar los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Mover la serpiente
            # self.snake_action.update(self.screen)
            self.update()

            self.snake_action.move()
            # Detecta coliciones
            self.detectCollition()
            # Dibujar los objetos en la pantalla
            self.draw()

            # Actualizar la pantalla
            pygame.display.flip()
            self.clock.tick(self.clock_speek)

    def detectCollition(self):
        # Verificar colisiones
        if self.snake_segments[0].rect.colliderect(self.food.rect):
            # Crear una nueva pieza de comida
            self.all_sprites.remove(self.food)
            self.food = Food(random.randint(0, self.width - 10), random.randint(0, self.height - 10))
            self.all_sprites.add(self.food)
            # La serpiente ha comido la comida
            # Aumentar el tamaño de la serpiente
            self.length += 5
            self.clock_speek += 2


    def update(self):
        if self.snake_segments[0].rect.x < 0 or self.snake_segments[0].rect.x > self.screen.get_width() or self.snake_segments[0].rect.y < 0 or self.snake_segments[0].rect.y > self.screen.get_height():
            pygame.quit()
            sys.exit()

        # Mueve la serpiente en la dirección actual
        head = self.snake_segments[0]
        new_x = head.rect.x + self.snake.direction[0] * head.rect.width
        new_y = head.rect.y + self.snake.direction[1] * head.rect.height

        # Añade un nuevo segmento en la posición actual de la cabeza
        new_segment = Snake(new_x, new_y, head.rect.width, head.rect.height)
        self.snake_segments.insert(0, new_segment)
        
        if(len(self.snake_segments)>self.length):
            self.snake_segments.pop()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        for segment in self.snake_segments:
            self.screen.blit(segment.image, segment.rect)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()