import pygame
import random

# --- Ініціалізація ---
pygame.init()
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 10

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# --- Кольори ---
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


font = pygame.font.SysFont("Arial", 24)

# --- Клас Змійки ---
class Snake:
    def __init__(self):
        self.body = [(5, 5)]
        self.direction = (1, 0)
        self.growing = False

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)
        if self.growing:
            self.growing = False
        else:
            self.body.pop()

    def grow(self):
        self.growing = True

    def draw(self, window):
        for segment in self.body:
            pygame.draw.rect(window, GREEN, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def check_collision(self):
        head = self.body[0]
        return (
            head in self.body[1:] or
            head[0] < 0 or head[0] >= WIDTH // CELL_SIZE or
            head[1] < 0 or head[1] >= HEIGHT // CELL_SIZE
        )

# --- Клас Їжі ---
class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        return (random.randint(0, WIDTH // CELL_SIZE - 1), random.randint(0, HEIGHT // CELL_SIZE - 1))

    def draw(self, window):
        pygame.draw.rect(window, RED, (self.position[0]*CELL_SIZE, self.position[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))


score = 0
snake = Snake()
food = Food()
running = True

while running:
    clock.tick(FPS)
    window.fill(BLACK)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Клавіші ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and snake.direction != (0, 1):
        snake.direction = (0, -1)
    if keys[pygame.K_s] and snake.direction != (0, -1):
        snake.direction = (0, 1)
    if keys[pygame.K_a] and snake.direction != (1, 0):
        snake.direction = (-1, 0)
    if keys[pygame.K_d] and snake.direction != (-1, 0):
        snake.direction = (1, 0)

    
    snake.move()

    
    if snake.body[0] == food.position:
        snake.grow()
        food = Food()
        score += 1

    
    if snake.check_collision():
        running = False

    
    snake.draw(window)
    food.draw(window)

    score_text = font.render(f"Очки: {score}", True, [255, 255, 255])
    window.blit(score_text, (10, 10))
    pygame.display.update()

pygame.quit()