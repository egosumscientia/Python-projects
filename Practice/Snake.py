import pygame
import random

from adodbapi.ado_consts import directions
from pygame.examples.sprite_texture import running

#Inicializar pygame
pygame.init()

#config de pantalla
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake - Procedural")

#Colores
BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#Fxn para generar comida aleatoria
def random_food():
    x = random.randint(0, (WIDTH // CELL_SIZE) -1) * CELL_SIZE
    y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
    return (x, y)

#Inicializacion de variables
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)
food = random_food()
clock = pygame.time.Clock()
score = 0

#Bucle principal
def game_loop():
    global direction, snake, food, score
    running = True
    while running:
        screen.fill(BLACK)

        #Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE ,0)

        #Mover la serpiente
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        #Verificar colisiones con los bordes o consigmo misma
        if (new_head in snake or new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT):
            running = False
            continue

        snake.insert(0, new_head)

        #Verificar si la serpiento comio la comida
        if new_head == food:
            score +=1
            food = random_food()
        else:
            snake.pop()

        #Dibujar la comida
        pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

        #Dibujar la serpiente
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

        #Actualizar la pantalla
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

#Ejecutar el juego
if __name__ == "__main__":
    game_loop()




















































