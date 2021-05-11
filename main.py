import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))

clock = pygame.time.Clock()

class Snake:
    def __init__(self, x, y, size, direction):
        self.x = x
        self.y = y
        self.x_speed = 20
        self.y_speed = 0
        self.width = 20
        self.height = 20
        self.direction = direction
        self.size = 1

    def drawSnake(self):
        self.width = self.width * self.size
        self.height = self.height * self.size
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def updateSnake(self):
        if self.direction == 'up':
            self.x_speed = 0
            self.y_speed = -20
        if self.direction == 'down':
            self.x_speed = 0
            self.y_speed = 20
        if self.direction == 'left':
            self.x_speed = -20
            self.y_speed = 0
        if self.direction == 'right':
            self.x_speed = 20
            self.y_speed = 0
        self.x += self.x_speed
        self.y += self.y_speed

    # def directionUpdate(self):
    #     keys = pygame.key.get_pressed()
    #     for key in keys:
    #         if key == pygame.K_UP:
    #             self.direction = 'up'
    #         if key == pygame.K_DOWN:
    #             self.direction = 'down'
    #         if key == pygame.K_LEFT:
    #             self.direction = 'left'
    #         if key == pygame.K_RIGHT:
    #             self.direction = 'right'


snake = Snake(0, 0, 1, 'right')


def drawGameWindow():
    screen.fill((0, 0, 0))
    snake.updateSnake()
    snake.drawSnake()
    pygame.display.update()


run = True
while run:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake.direction = 'up'
    if keys[pygame.K_DOWN]:
        snake.direction = 'down'
    if keys[pygame.K_LEFT]:
        snake.direction = 'left'
    if keys[pygame.K_RIGHT]:
        snake.direction = 'right'

    drawGameWindow()

pygame.quit()