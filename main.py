import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 600))

clock = pygame.time.Clock()

run = True

class Snake:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.x_speed = 20
        self.y_speed = 0
        self.width = 20
        self.height = 20
        self.size = 1

    def drawSnake(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def updateSnake(self):
        global run
        global frameCount
        if frameCount == 2:
            self.x += self.x_speed
            self.y += self.y_speed
            if self.x < 0 or self.x > 600:
                run = False
            if self.y < 0 or self.y > 600:
                run = False
            frameCount = 0


class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0, 255, 0)

    def drawApple(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 20, 20))

    def updateApple(self):
        if self.x == snakeHead.x and self.y == snakeHead.y:
            snakeHead.size += 1
            self.x = random.randrange(0, 600, 20)
            self.y = random.randrange(0, 600, 20)


snakeHead = Snake(0, 0, 1)
apple = Apple(300, 300)

def drawGameWindow():
    global run
    screen.fill((0, 0, 0))
    snakeHead.updateSnake()
    apple.drawApple()
    snakeHead.drawSnake()
    pygame.display.update()

frameCount = 0
while run:
    clock.tick(20)
    frameCount += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snakeHead.x_speed = 0
        snakeHead.y_speed = -20
    if keys[pygame.K_DOWN]:
        snakeHead.x_speed = 0
        snakeHead.y_speed = 20
    if keys[pygame.K_LEFT]:
        snakeHead.x_speed = -20
        snakeHead.y_speed = 0
    if keys[pygame.K_RIGHT]:
        snakeHead.x_speed = 20
        snakeHead.y_speed = 0

    apple.updateApple()
    drawGameWindow()

pygame.quit()