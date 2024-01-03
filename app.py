import pygame, sys
import random
from src.Snake import Snake;
from src.Food import Food;

pygame.init()
# Screen
size = width, height = 1366, 768
screen = pygame.display.set_mode(size)

# 
snake = Snake()
food = Food(200, 200)

#
all_sprites = pygame.sprite.Group()
all_sprites.add(snake)
all_sprites.add(food)

while True:
    # Procesar los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Mover la serpiente
    snake.update(screen)
    snake.move()

    # Verificar colisiones
    if snake.rect.colliderect(food.rect):
        # Crear una nueva pieza de comida
        all_sprites.remove(food)
        food = Food(random.randint(0, width - 10), random.randint(0, height - 10))
        all_sprites.add(food)
        # La serpiente ha comido la comida
        # Aumentar el tamaño de la serpiente
        snake.length += 10
        snake.grow()
        

    # Dibujar los objetos en la pantalla
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
       
    # Actualizar la pantalla
    pygame.display.flip()