import pygame
import sys
import random
import json
from src.snake import Snake;
from src.snake_actions import SnakeActions;
from src.food import Food;

class SnakeGame:
    def __init__(self, config):
        pygame.init()
        pygame.font.init()  # Inicializa la biblioteca de fuentes

        self.config_file = config
        # Screen
        self.width = config["screen"]["width"]
        self.height = config["screen"]["height"]
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        # 
        self.snake = Snake(
                        config["snake"]["pos_x"], 
                        config["snake"]["pos_y"], 
                        config["snake"]["width"],
                        config["snake"]["height"],
                        config["snake"]["color_init"]
                    )
        self.snake_segments = [self.snake]
        self.snake_action = SnakeActions(self.snake)
        self.food = Food(
            config["food"]["pos_x"], 
            config["food"]["pos_y"], 
            config
        )

        #
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.snake)
        self.all_sprites.add(self.food)

        self.length = config["snake"]["length"]
        self.clock_speed = config["speed"]["clock"]
        self.font_score = pygame.font.Font(None, 60)
        self.score=0
    
    def run(self):
        while True:
            # Procesar los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Mover la serpiente
            self.update()
            self.snake_action.move()
            # Detecta coliciones
            self.detectCollition()
            
            # Dibujar los objetos en la pantalla
            self.draw()
            #
            self.font()
            # Actualizar la pantalla
            self.updateScreen()


    def detectCollition(self):
        # Verificar colisiones serpiente y comida
        if self.snake_segments[0].rect.colliderect(self.food.rect):
            # Crear una nueva pieza de comida
            self.all_sprites.remove(self.food)
            self.food = Food(random.randint(0, self.width - 10), random.randint(0, self.height - 10), self.config_file)
            self.all_sprites.add(self.food)
            # La serpiente ha comido la comida
            # Aumentar el tamaño de la serpiente
            self.length += self.config_file["speed"]["snake_grow_sp"]
            self.clock_speed += self.config_file["speed"]["clock_speed"]
            self.score+=1
        # Detecta colision serpiente con sigo misma
        for snake_coll in self.snake_segments[1:]:
            if self.snake_segments[0].rect.colliderect(snake_coll.rect):
                pygame.quit()
                sys.exit()

    def update(self):
        if self.snake_segments[0].rect.x < 0 or self.snake_segments[0].rect.x > self.screen.get_width() or self.snake_segments[0].rect.y < 0 or self.snake_segments[0].rect.y > self.screen.get_height():
            pygame.quit()
            sys.exit()

        # Mueve la serpiente en la dirección actual
        head = self.snake_segments[0]
        new_x = head.rect.x + self.snake.direction[0] * head.rect.width
        new_y = head.rect.y + self.snake.direction[1] * head.rect.height

        # Añade un nuevo segmento en la posición actual de la cabeza
        new_segment = Snake(new_x, new_y, head.rect.width, head.rect.height, self.config_file["snake"]["color"])
        self.snake_segments.insert(0, new_segment)
        
        if(len(self.snake_segments) > self.length):
            self.snake_segments.pop()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        for segment in self.snake_segments:
            self.screen.blit(segment.image, segment.rect)

    def updateScreen(self):
        pygame.display.flip()
        self.clock.tick(self.clock_speed)

    def font(self):        
        text = self.font_score.render(f"Score: {self.score}", True, (255,255,255))
        post_text_p1_x = self.width-(self.width*0.2)
        post_text_p1_y = self.height-(self.height*.1)
        self.screen.blit(text, (post_text_p1_x, post_text_p1_y))

def init(config_file):
    with open(config_file, 'r') as file:
        config_data = json.load(file)
    return config_data

if __name__ == "__main__":
    config = init(".\config.json")
    game = SnakeGame(config)
    game.run()