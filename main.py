import pygame
import random
import time

class Square:
    def __init__(self, x, y, width=20, height=20,color= (255, 255, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hitbox = pygame.Rect(x,y,width,height)

    def draw(self, window):
        pygame.draw.rect(window, self.color,self.hitbox)

    def update(self):
        pass


class Apple:
    def __init__(self, width=20, height=20, color=(255, 0, 0)):
        self.x = random.randint(0,690)
        self.y = random.randint(0,490)
        self.width = width
        self.height = height
        self.color = color
        self.hitbox = pygame.Rect(self.x, self.y, width, height)


    def draw(self, window):
        pygame.draw.rect(window, self.color,self.hitbox)

    def update(self):
        self.x = random.randint(0,690)
        self.y = random.randint(0,490)
        self.hitbox.x = self.x
        self.hitbox.y = self.y


snake = [Square(100, 100), Square(80, 100)]
snake.append(Square(60, 100))

lastupdate = 0


pygame.init()
window = pygame.display.set_mode([700, 500])
clock = pygame.time.Clock()
hero = Square(299,244,20,20,color = (255, 255, 0))

fon_jpg = pygame.image.load("fon.jpg")
fon_jpg = pygame.transform.scale(fon_jpg, [700,500])
speed_x = 0
speed_y = -20
apple = Apple()
apple.update()

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    speed_x = 20
                    speed_y = 0
                if event.key == pygame.K_a:
                    speed_x = -20
                    speed_y = 0
                if event.key == pygame.K_w:
                    speed_x = 0
                    speed_y = -20
                if event.key == pygame.K_s:
                    speed_x = 0
                    speed_y = 20

    head = snake[0]
    if (head.hitbox.x < 0 or head.hitbox.x >= 700 or
                    head.hitbox.y < 0 or head.hitbox.y >= 500):
                    snake = [Square(100, 100), Square(80, 100), Square(60, 100)]
                    speed_x, speed_y = 0, -20
                    apple.update()

    if snake[0].hitbox.colliderect(apple.hitbox):
                apple.update()
                snake.append(Square(snake[-1].x, snake[-1].y))
                

                
                    

    hero.update()
    

    if time.time() - lastupdate > 0.3:


        snake.insert(0,Square(snake[0].hitbox.x+speed_x,(snake[0].hitbox.y+speed_y)))
        snake.pop()
        lastupdate = time.time()
    window.blit(fon_jpg, [0,0])
    hero.draw(window)
    apple.draw(window)
    for segment in snake:
         segment.draw(window)
    pygame.display.flip()
    clock.tick(60)