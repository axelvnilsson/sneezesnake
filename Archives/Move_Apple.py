import pygame
import random

# initialize pygame
pygame.init()

# set up screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

clock = pygame.time.Clock()

# initial position of the apple
apple_x = random.randint(0, screen_width-20)
apple_y = random.randint(0, screen_height-20)

# game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # move the apple
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        apple_x += 5
    if keys[pygame.K_LEFT]:
        apple_x -= 5
    if keys[pygame.K_DOWN]:
        apple_y += 5
    if keys[pygame.K_UP]:
        apple_y -= 5

    # check boundaries
    if apple_x < 0:
        apple_x = 0
    elif apple_x > screen_width - 20:
        apple_x = screen_width - 20
    if apple_y < 0:
        apple_y = 0
    elif apple_y > screen_height - 20:
        apple_y = screen_height - 20

    # draw the apple
    pygame.draw.rect(screen, RED, (apple_x, apple_y, 20, 20))

    pygame.display.update()
    clock.tick(40)

pygame.quit()