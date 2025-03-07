import pygame
import  random

#Config
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Snake:
    def __init__(self):
        self.body = [(100,100),(80,100),(60,100)]
        self.direction = (CELL_SIZE, 0)

    def move(self):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0 ,new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self):
        head = self.body[0]
        return head in self.body[1:] or head[0]<0 or head[0]>=WIDTH or head[1]<0 or head[1]>=HEIGHT

    def set_direction(self, direction):
        if (direction[0]*-1, direction[1]*-1) != self.direction:
            self.direction = direction

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN,(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        x = random.randint(0, (WIDTH//CELL_SIZE)-1) * CELL_SIZE
        y = random.randint(0, (HEIGHT//CELL_SIZE)-1) * CELL_SIZE
        return (x,y)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake - POO")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.running = True
        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.set_direction((0, -CELL_SIZE))
                elif event.key == pygame.K_DOWN:
                    self.snake.set_direction((0, CELL_SIZE))
                elif event.key == pygame.K_LEFT:
                    self.snake.set_direction((-CELL_SIZE, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.set_direction((CELL_SIZE, 0))

    def update(self ):
        self.snake.move()
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.position = self.food.random_position()
            self.score+=1
        if self.snake.check_collision():
            self.running = False


    def draw(self):
        self.screen.fill(BLACK)
        self.food.draw(self.screen)
        self.snake.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)
        pygame.quit()

if __name__ == "__main__":
    Game().run()


















